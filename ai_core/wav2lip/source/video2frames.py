import cv2
import os
import argparse
import shutil
parser = argparse.ArgumentParser(description='code for extracting frames from video')

parser.add_argument('--input_video', type=str, help='Video path to save result. See default for an e.g.', 
                                default='ai_core/wav2lip/output_preHD')

parser.add_argument('--frames_path', type=str, help='Video path to save result. See default for an e.g.', 
                                default='ai_core/wav2lip/frame_preHD')

args = parser.parse_args()
def extract_video_to_frame():
    shutil.rmtree(args.frames_path, ignore_errors=True)
    # Read the video file
    video_dir = args.input_video
    folder = os.listdir(video_dir)
    file_names = ["ai_core/wav2lip/output_preHD/" + file_name for file_name in folder]
    frame_index = 0
    for video_path in file_names:
        video = cv2.VideoCapture(video_path)

        # Get the frames per second (fps) and duration of the video
        fps = int(video.get(cv2.CAP_PROP_FPS))
        duration = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # Create a folder to store the extracted frames
        frame_folder = args.frames_path
        os.makedirs(frame_folder, exist_ok=True)

        # Initialize a counter for the frame index
        
        # Loop through each frame of the video and save it as an image file
        for i in range(duration):
            ret, frame = video.read()
            if not ret:
                break
            # Save the frame as an image file in the frame folder
            frame_file = os.path.join(frame_folder, f'frame_{frame_index:05d}.jpg')
            cv2.imwrite(frame_file, frame)
            frame_index += 1


        video.release()