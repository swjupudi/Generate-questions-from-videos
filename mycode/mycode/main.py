#Initialize OpenAI API
from openai import OpenAI
import os
from mycode import prompts
from moviepy.editor import VideoFileClip
import tempfile


# Function to extract audio from video to send whisper model

def extract_audio_from_uploaded_video(uploaded_video):
    """
    Extracts audio from a video file uploaded through Streamlit.

    Args:
        uploaded_video (UploadedFile): The uploaded video file object from Streamlit.
    """
    try:
        # Create a temporary file to save the uploaded video
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmpfile:
            # Write the uploaded video content to the temporary file
            tmpfile.write(uploaded_video.read())
            tmpfile_path = tmpfile.name
        
        # Load the video file from the temporary file path
        video = VideoFileClip(tmpfile_path)
        
        # Extract the audio
        audio = video.audio
        return audio
        
    except Exception as e:
        print(f"Failed to extract audio: {e}")
    
    


# Function to transcribe video using OpenAI's Whisper model
def transcribe_video(video_file):
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY_ST'))
    audio_clip = extract_audio_from_uploaded_video(video_file)
   # Create a temporary audio file
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmpfile:
        audio_file_path = tmpfile.name
    
    # Save the audio clip to the temporary file
    audio_clip.write_audiofile(audio_file_path, codec='mp3')
    
    # Now, you can use the file path to pass to the transcription service
    with open(audio_file_path, 'rb') as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model='whisper-1'  # Specify the model name if required
        )
    
    os.remove(audio_file_path)
    
    return response
    
#Generate questions
def generate_quiz(text,n_questions, difficulty):
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY_ST'))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=prompts.generate_quizbot_prompts(text,n_questions, difficulty),
        temperature=0.7
    )
    return response.choices[0].message.content 