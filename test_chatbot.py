import sys
import os

# Fix module path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from modules.chatbot import get_answer

questions = [
    "College ka naam kya hai?",
    "Fees kitni hai?",
    "AI ML course available hai?",
    "Placement hoti hai?"
]

for q in questions:
    print("Question:", q)
    print("Answer:", get_answer(q))
    print("-" * 50)