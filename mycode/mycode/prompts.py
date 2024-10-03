import typing as t


def generate_quizbot_prompts(
    text: str,
    n_questions: int = 5,
    difficulty: t.Literal["easy", "medium", "hard"] = "medium",
):
    quizbot_prompts = [
        {
            "role": "system",
            "content": "You are a helpful tutor skilled at generating quiz questions from the study material provided.",
        },
        {
            "role": "user",
            "content": f"Generate {n_questions} multiple choice quiz questions from the following text {text}.the difficulty level should be {difficulty}.",
        },
    ]
    return quizbot_prompts
