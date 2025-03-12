import streamlit as st
import random
import time

st.set_page_config(page_title="Quiz App ",page_icon=":material/quiz:",layout="centered")

st.title("Quiz App 📃")
questions =[
    {  
      "question": "What is the capital of France?",
      "options": ["Paris", "Marseille", "Lyon"], 
      "answer": "Paris" ,
    },
    {  
      "question": "What is the capital of Japan? ",
      "options": ["Osaka", "Kyoto", "Tokyo"],  
      "answer": "Tokyo"  
    },
    {  
      "question": "What is the capital of Brazil? ",
      "options": ["Rio de Janeiro", "São Paulo", "Brasília"],  
      "answer": "Brasília"  
    },
    {  
      "question": "What is the capital of Australia? ",
      "options": ["Sydney", "Melbourne", "Canberra"],  
      "answer": "Canberra"  
    },
    {  
      "question": "What is the capital of Canada? ",
      "options": ["Toronto", "Vancouver", "Ottawa"],  
      "answer": "Ottawa"  
    },
  
]

#session state is a function like usestate which remembers the state of the application and store in browser memory
if "current_question" not  in st.session_state:
    st.session_state.current_question = random.choice(questions)
question =  st.session_state.current_question

st.subheader(question["question"])
selected_option = st.radio("Select Your Answer",question["options"],key="answer")

if st.button("Submit!"):
    if selected_option == question["answer"]:
        st.success("Correct answer 🎉")
    else:
        st.error("Incorrect Answer ❌ ,The correct answer is " + question["answer"])
    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()   
