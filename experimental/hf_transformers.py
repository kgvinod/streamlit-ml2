from transformers import AutoTokenizer, AutoModel
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/oasst-sft-1-pythia-12b")
model = AutoModelForCausalLM.from_pretrained("OpenAssistant/oasst-sft-1-pythia-12b")

inputs = tokenizer("I am smart because ", return_tensors="pt")
outputs = model(**inputs)
print(outputs)