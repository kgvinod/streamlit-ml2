import openai
import json

class QuizCreator():

    def generate_quiz(self, topic_text):

        # Set up OpenAI API
        openai.api_key = "keY"

        num_questions = 3
        #prompt = f"Generate {num_questions} multiple-choice questions with 4 answer choices each."
        #prompt = f"Generate {num_questions} multiple-choice questions about {new_quiz.title_text} with response in JSON formatted 'questions' array. Each question should have a 'question_line' containing the question text, a 'choices' array containing 'choice' and 'is_correct' flag."
        #prompt = f"Generate {num_questions} multiple-choice questions about the topic {new_quiz.title_text}. The response must be JSON with a 'description' about the topic and a 'questions' array. Each question should have a 'question_line' containing the question text, a 'choices' array containing 'choice' and 'is_correct' flag."
        prompt = f"Generate {num_questions} multiple-choice questions about the topic {topic_text}. The response must be JSON with a correctly punctuated 'topic', a 'description' about the topic and a 'questions' array. Each question should have a 'question_line' containing the question text, a 'choices' array containing 'choice' and 'is_correct' flag."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                        #{"role": "system", "content": "You are a REST API endpoint that responds in JSON"},
                        {"role": "user", "content": prompt}
                        ],
        )

        response_message = response.choices[0].message.content
        print(response_message)
        
        # Remove json markup
        response_json = response_message.replace('```', "")
        response_json = response_json.replace('json', "")

        # Parse JSON response
        data = json.loads(response_json)
        print(data)    
        
        return data

