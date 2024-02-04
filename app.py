import streamlit as st
#from openai_qk import QuizCreator
from langchain_qk import QuizCreator
import json

def main():
    st.set_page_config(page_title="Quiz App", page_icon=":question:", layout="centered", initial_sidebar_state="auto")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Blog", "About"])

    if page == "Home":
        home()
    elif page == "Blog":
        blog()
    elif page == "About":
        about()


def home():

    st.title("Quiz Generator")

    if "topic" not in st.session_state:
        st.session_state.topic = ''

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = json.loads('{}')

    if "submitted_questions" not in st.session_state:
        st.session_state.submitted_questions = set()        

    if "correct_answers" not in st.session_state:
        st.session_state.correct_answers = set()        
       
    user_input = st.empty()
    user_topic = user_input.text_input("Enter the topic for the quiz:", key=f"text-input-01")
    print("Read input", user_topic)

    if user_topic:
        if st.session_state.topic != user_topic:
            print("Generating quiz for", user_topic)
            
            with st.spinner('Creating quiz for ' + user_topic + '...'):
                #user_input.empty()
                quiz_data = QuizCreator().generate_quiz(user_topic)
                st.session_state.correct_answers = set()

            st.session_state.topic = user_topic
            st.session_state.quiz_data = quiz_data
        
        quiz_data = st.session_state.quiz_data
        questions = quiz_data["questions"]

        st.write(quiz_data["description"])

        print("Displaying quiz for", user_topic)
        for question in questions:
            display_question(question)

        score_str = ":blue[Score: " + str(len(st.session_state.correct_answers)) + '/' + str(len(quiz_data["questions"])) +']'
        if str(len(st.session_state.correct_answers)) == str(len(quiz_data["questions"])):
            score_str += ' :sunglasses:'
        st.header(score_str)



def display_question(question):
    st.subheader(question["question_line"])
    choices = question["choices"]
    radio_key = f"radio-{question['question_line']}"
    is_disabled = question["question_line"] in st.session_state.submitted_questions

    user_answer = st.radio("", [choice["choice"] for choice in choices], key=radio_key, disabled=is_disabled)

    if not is_disabled:
        submit_button = st.empty()
        if submit_button.button("Submit", key=f"submit-{question['question_line']}"):
            correct_answer = next(choice for choice in choices if choice["is_correct"])["choice"]
            submit_button.empty()
            if user_answer == correct_answer:
                st.success("Correct!")
                st.session_state.correct_answers.add(question["question_line"])
            else:
                st.error(f"Wrong! The correct answer is {correct_answer}.")
            st.session_state.submitted_questions.add(question["question_line"])
            st.experimental_rerun()

    else:
        correct_answer = next(choice for choice in choices if choice["is_correct"])["choice"]
        if user_answer == correct_answer:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is {correct_answer}.")

def blog():
    st.title("Blog")

def about():
    st.title("About")

if __name__ == "__main__":
    main()
