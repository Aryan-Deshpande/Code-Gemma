import torch
from transformers import AutoTokenizer
from trl import PPOConfig, AutoModelForCausalLMWithValueHead, create_reference_model
from trl.core import respond_to_batch

model = AutoModelForCausalLMWithValueHead.from_pretrained('gpt2')
model_ref = create_reference_model(model)

tokenizer = AutoTokenizer.from_pretrained('gpt2')

ppo_config = PPOConfig(
    batch_size=1
)

query_txt = "Wow there is a lot of sun today"
query_tensor = tokenizer.encode(query_txt, return_tensors="pt")

response_tensor = respond_to_batch(model, query_tensor)


