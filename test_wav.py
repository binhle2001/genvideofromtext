import subprocess
import os

def convert_frames_to_video(input_folder="REAL_ESRGAN/output", output_video_path="output_video.mp4", audio_path="wav2lip/data/output/output_audio.wav", fps = 25):
    # image_files = [os.path.join(input_folder, f'frame_{i:05d}_out.jpg') for i in range(len(os.listdir(input_folder)))]

    ffmpeg_command = f'ffmpeg -r {fps} -i {input_folder}/frame_%05d_out.jpg -i {audio_path} -c:v libx264 -crf 25 -preset veryslow -acodec aac -strict experimental {output_video_path}'
    
    
    
    subprocess.run(ffmpeg_command, shell=True)
    
convert_frames_to_video()
