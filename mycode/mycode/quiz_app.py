import streamlit as st
from mycode import main
import os


# Streamlit app
st.title('Video Quiz Generator')

#Take OpenAI api key as input and store it in an environment variable
api_key = st.text_input("Enter your OpenAI API key", type='password')
os.environ['OPENAI_API_KEY_ST'] = api_key



video_file = st.file_uploader("Upload your video here", type=['mp4'])




#Handle video file uploaded by showing a success message
if video_file is not None:
    st.write("Video uploaded successfully. Video transcription now in progress.")

#Generate quiz questions
if video_file is None:
    st.write("Please upload a video file to generate a quiz")
else:
    transcription = main.transcribe_video(video_file)
    
    n_questions = st.number_input("How many questions do you want to generate?", min_value=1, value=5)
    difficulty = st.selectbox("Select the difficulty level of the questions", ['easy', 'medium', 'hard'])
    
    if st.button('Generate Quiz'):
        questions = main.generate_quiz(transcription.text, n_questions=n_questions, difficulty=difficulty)
        st.markdown(f"Test your knowledge:\n {questions}")