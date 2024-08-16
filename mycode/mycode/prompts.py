

def generate_quizbot_prompts(text,n_questions=5, difficulty='medium'):
    quizbot_prompts = [
    {
    "role": 'system',
    "content": "You are a helpful tutor skilled at generating quiz questions from the study material provided."
    },
    {
    "role": 'user',
    "content": f"Generate {n_questions} multiple choice quiz questions from the following text {text}.the difficulty level should be {difficulty}."
    },
    ]
    return quizbot_prompts
