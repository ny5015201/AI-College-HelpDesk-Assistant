# modules/chatbot.py

import pandas as pd
from difflib import get_close_matches

# Load dataset
def load_dataset():
    data = pd.read_csv("dataset/college_faq.csv")
    return data

# Find best answer
def get_answer(user_question):
    data = load_dataset()
    
    questions = data['Question'].tolist()
    
    # Find closest matching question
    match = get_close_matches(user_question, questions, n=1, cutoff=0.4)
    
    if match:
        matched_question = match[0]
        answer = data.loc[data['Question'] == matched_question, 'Answer'].values[0]
        return answer
    else:
        return "Sorry, mujhe is question ka exact answer nahi mila. Please try another query."