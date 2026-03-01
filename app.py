import streamlit as st
from modules.chatbot import get_answer

st.set_page_config(page_title="AI College Help Desk Assistant")

st.title("🎓 AI College Help Desk Assistant")
st.write("Ask any question related to college (admission, fees, placement, etc.)")

# User input
user_question = st.text_input("💬 Type your question here:")

# When user enters question
if user_question:
    answer = get_answer(user_question)
    st.success(answer)