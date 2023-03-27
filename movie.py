from moviepy.editor import VideoFileClip, concatenate_videoclips

def generate_movie(num_parts):
    # List of video file names to concatenate
    video_files = []

    for i in range(num_parts):
        video_files.append(f"output_video{i + 1}.mp4")

    # Load each video file as a video clip
    clips = [VideoFileClip(file) for file in video_files]

    # Concatenate the video clips into one clip
    final_clip = concatenate_videoclips(clips)

    # Set the frame rate of the final clip to 24 fps
    final_clip.fps = 24

    # Set the output video file name
    output_video = "trailer.mp4"

    # Write the final clip to a video file
    final_clip.write_videofile(output_video, codec='libx264', audio_codec='aac')
