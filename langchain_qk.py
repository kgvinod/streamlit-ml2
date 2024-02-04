import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import json

class QuizCreator():

    def generate_quiz(self, topic_text):

        # Set up OpenAI API
        os.environ['OPENAI_API_KEY'] = "keY"

        num_questions = 5
        #prompt = f"Generate {num_questions} multiple-choice questions with 4 answer choices each."
        #prompt = f"Generate {num_questions} multiple-choice questions about {new_quiz.title_text} with response in JSON formatted 'questions' array. Each question should have a 'question_line' containing the question text, a 'choices' array containing 'choice' and 'is_correct' flag."
        #prompt = f"Generate {num_questions} multiple-choice questions about the topic {new_quiz.title_text}. The response must be JSON with a 'description' about the topic and a 'questions' array. Each question should have a 'question_line' containing the question text, a 'choices' array containing 'choice' and 'is_correct' flag."
        prompt = f"Generate {num_questions} multiple-choice questions about the topic {topic_text}. The response must be JSON with a correctly punctuated 'topic', a 'description' about the topic and a 'questions' array. Each question should have a 'question_line' containing the question text, a 'choices' array containing 'choice' and 'is_correct' flag."
        #prompt = f"Generate {num_questions} MCQs about {topic_text} in JSON with a correctly punctuated 'topic', a concise 'description' about the topic and a 'questions' array. Each question should have a 'question_line', a 'choices' array with 'choice' and 'is_correct' flag."

        # LLMs
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)
        messages = [
            #SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content=prompt)
        ]

        response = llm(messages)
        print(response)
        
        # Parse JSON response
        data = json.loads(response.content)
        print(data)    
        
        return data


