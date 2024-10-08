<!-- ABOUT THE PROJECT -->
## About The Project

This project leverages the power of OpenAI's Whisper model to transcribe videos and generate quiz questions based on the transcriptions. The workflow involves uploading a video file, which is then processed by the Whisper model to produce a text transcription. Using this transcription, OpenAI's language model generates relevant quiz questions, making it an effective tool for educational purposes, content review, and interactive learning.

### Key Features

- **Video Transcription**: Utilizes OpenAI's Whisper model to accurately transcribe the audio content of uploaded videos.
- **Quiz Generation**: Automatically generates quiz questions from the transcribed text using OpenAI's language model.
- **Interactive Learning**: Facilitates an engaging way to review and reinforce the content of the video through generated quizzes.



## Getting Started

Follow these steps to get started with the project. 

### Prerequisites

- Python 3.6 or higher
- Anaconda to create new environment
- **Obtain OpenAI API Key:**
   - Sign up on the [OpenAI website](https://www.openai.com/) if you haven't already.
   - Generate an API key from the OpenAI dashboard.
- Ensure you have a video file of MP4 format ready for generating the quiz content.


### Installing

1. **Clone the repository:**

```
git clone git@github.com:swjupudi/Generate-questions-from-videos.git
```


2. **Create and activate a virtual environment:**

- Navigate to the project directory:
  ```
  cd <path/to/project>
  ```
- Create a virtual environment:
  ```
  conda create -n <environment name> python==3.12
  ```
  Eg: 
   ```
  conda create -n quiz_from_videos python==3.12
  ```
- Activate the virtual environment:
  - On macOS/Linux:

    ```
    conda activate <environment name>
    ``` 
    Eg
    ```
    conda activate quiz_from_videos
    ```
  - pip install ipykernel

3. **Install dependencies:**

With the virtual environment activated, install the requirements using:

```
pip install -r requirements.txt
```

### Executing the Project
- With your virtual environment activated and dependencies installed, start the Streamlit application:
     ```
     streamlit run quiz_app.py
     ```
- This command will launch the application, typically accessible at `http://localhost:5000/`


## Code Walkthrough

1. Quiz_app.py
    
    This will open up a web page
    
    User will need to input their openai key, upload the video
    
    The transcribe_video function from [main.py](http://main.py) is then called to transcribe the video. Out put is stored in transcription object.
    
    User then enters the number of questions he wants to be generated ( Range is only between 1 to 5) and clicks generate quiz
    
    The generate_quiz function from [main.py](http://main.py) is then called and the result is stored in questions

2. main.py
    
    This has 3 functions:
    
    extract_audio_from_uploaded_video using moviepy.editor
    
    transcribe_video using whisper model
    
    generate_quiz using gpt-4o
    
    doing exactly what the function name suggests.

Here's how the output looks like

<img width="609" alt="Screenshot 2024-08-18 at 12 24 27 PM" src="https://github.com/user-attachments/assets/54b3e754-c90f-44af-805d-2968bb2e615c">
<img width="699" alt="Screenshot 2024-08-18 at 12 24 56 PM" src="https://github.com/user-attachments/assets/f74b850e-5900-403a-8b3b-3003f55b066d">