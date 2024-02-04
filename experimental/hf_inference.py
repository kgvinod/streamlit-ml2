import requests

#API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-1-pythia-12b"
#API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-7-llama-30b-xor"
#API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/stablelm-7b-sft-v7-epoch-3"
#API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-1-pythia-12b"
API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stablelm-tuned-alpha-3b"
API_URL = "https://api-inference.huggingface.co/models/nomic-ai/gpt4all-j"
headers = {"Authorization": "Bearer KEY"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
prompt = "Write a quiz for AP biology chapter 2. There must be 3 questions. Each question has 4 choices. Return in JSON format."
#prompt = "Write c function to calculate factorial"
#prompt = "He was awarded the Nobel Prize in Peace in 2009 framed as a question "
#prompt = "Write Java class to calculate factorial."
#prompt = "One sentence for what happened in 1947 in India"
#prompt = "10 facts about Narendra Modi."
#prompt = "Next president of USA wil be "
#prompt = "The chance of Trump winning the next presidential election is  "
#prompt = "Write a short paragraph about using Arduino RP2040 to build a home security system."
#prompt = "Write quiz about Arduino with 3 questions and 4 answer choices."
#prompt = "Create 3 questions on Sacramento. Indicate questions with Q. Indicate answer choices with A,B,C,D. Indicate correct answer with *."
prompt = "Create 3 MCQs on Sacramento and return in JSON format."


output = query({
	"inputs": prompt,
    "parameters": {"do_sample": False, "max_new_tokens": 250},
})

print()
try:
    print (output[0]['generated_text'])
except Exception as e:
    print(output)
print()
