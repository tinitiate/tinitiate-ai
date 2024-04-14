# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="distilbert/distilgpt2")


# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")