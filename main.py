import os
from ai_core.REAL_ESRGAN.inference_realesrgan import frame_to_HD
from ai_core.tts.source.synthesizer import convert_text_to_speech
from helpers.config_s3 import s3
from helpers.config_sqs import sqs
from pydub import AudioSegment
from ai_core.wav2lip.source.inference import add_lip
from ai_core.wav2lip.source.video2frames import extract_video_to_frame
import subprocess
import shutil
import time
from datetime import datetime
from helpers.common import get_env_var
import helpers.download_pretrained
import requests
import json


def convert_frames_to_video(input_folder="ai_core/REAL_ESRGAN/output", output_video_path="ai_core/wav2lip/data/output/output_video.mp4", audio_path="ai_core/wav2lip/data/output/output_audio.wav", fps = 25):
    ffmpeg_command = f'ffmpeg -r {fps} -i {input_folder}/frame_%05d_out.jpg -i {audio_path} -c:v libx264 -crf 25 -preset veryslow -acodec aac -strict experimental {output_video_path}'
    
    subprocess.run(ffmpeg_command, shell=True)

def text_to_video(text, image_url, speed = 1, vocal = "female", language = "VI"):
    shutil.rmtree("ai_core/wav2lip/data/input/images", ignore_errors=True)
    os.makedirs("ai_core/wav2lip/data/input/images", exist_ok=True)
    file_local = "ai_core/wav2lip/data/input/images/image.jpg"
    response = requests.get(image_url)
    if response.status_code == 200:
        open(file_local, "wb").write(response.content)
    shutil.rmtree("ai_core/wav2lip/data/output", ignore_errors=True)
    os.makedirs("ai_core/wav2lip/data/output", exist_ok=True)
    convert_text_to_speech(text, speed= speed, vocal= vocal, language=language)
    add_lip(file_local) 
    extract_video_to_frame()
    frame_to_HD()
    convert_frames_to_video()
    return "ai_core/wav2lip/data/output/output_video.mp4"

def main():
    while True:
        response = sqs.receive_message(
            QueueUrl=get_env_var("s3", "AWS_QUEUE_INPUT_URL"),
            MaxNumberOfMessages=1,
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        if 'Messages' in response:
            received_message = response['Messages'][0]
            receipt_handle = received_message['ReceiptHandle']
            parsed_body = json.loads(received_message["Body"])
            print(parsed_body)
            video_id = parsed_body["video_id"]
            text_input = parsed_body["text_input"]
            image_url = parsed_body["character_url"]
            speed = float(parsed_body["speed"])
            language = parsed_body["language"]
            vocal = parsed_body["vocal"]
            try:
                video_output_file_name = text_to_video(text_input, image_url, speed, vocal, language)
                # Get the current date and time
                current_datetime = datetime.now()
                # Extract the date component
                current_date = current_datetime.date()
                video_output_file_name_s3 = f"video/{current_date}/{video_id}.mp4"

                with open(video_output_file_name, "rb") as f:
                    s3.upload_fileobj(f, get_env_var('s3', 'AWS_S3_BUCKET_NAME'), video_output_file_name_s3)
                
                message_body = {
                    'video_id': video_id,
                    'video_url': f"https://{get_env_var('s3', 'AWS_S3_BUCKET_NAME')}.s3.{get_env_var('s3', 'AWS_REGION_NAME')}.amazonaws.com/{video_output_file_name_s3}",
                    "status": "Done"
                }
                # Xác nhận xử lý xong thông điệp để nó không xuất hiện trong hàng đợi nữa
                
                request = sqs.send_message(
                    QueueUrl=get_env_var("s3", "AWS_QUEUE_OUTPUT_URL"),
                    MessageBody=json.dumps(message_body)  # Convert the dict to a JSON string before sending
                )
                sqs.delete_message(QueueUrl=get_env_var("s3", "AWS_QUEUE_INPUT_URL"), ReceiptHandle=receipt_handle)
            except Exception as e:
                message_body = {
                    'video_id': video_id,
                    'video_url': None,
                    "status": f"Failed with error {e}"
                }
                request = sqs.send_message(
                    QueueUrl=get_env_var("s3", "AWS_QUEUE_OUTPUT_URL"),
                    MessageBody=json.dumps(message_body)  # Convert the dict to a JSON string before sending
                )
            time.sleep(5)
        else:
            print("No messages in the queue. Waiting for 30 seconds...")
            time.sleep(30)  # Chờ 30 giây trước khi thử lại
            
main()




