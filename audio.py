from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

def generate_movie_clip(text, counter):
    # Create a gTTS object and set the language
    tts = gTTS(text=text, lang='en')

    # Set the output audio file name
    output_audio = f"output_audio{counter + 1}.mp3"

    # Save the audio file
    tts.save(output_audio)

    # Set the input image file name
    input_image = f"storyboardimage{counter + 1}.jpg"

    # Set the output video file name
    output_video = f"output_video{counter + 1}.mp4"

    # Load the image as a video clip
    clip_image = ImageClip(input_image)

    # Load the audio file as a video clip
    clip_audio = AudioFileClip(output_audio)

    # Set the duration of the image clip to match the duration of the audio clip
    clip_image = clip_image.set_duration(clip_audio.duration)

    # Combine the image and audio into a video clip
    final_clip = CompositeVideoClip([clip_image.set_audio(clip_audio)])

    # Set the frame rate of the final clip to 24 fps
    final_clip.fps = 24

    # Save the final video clip as an MP4 file
    final_clip.write_videofile(output_video, codec='libx264', audio_codec='aac')
