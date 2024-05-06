from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

checkpoint = "Salesforce/codegen-350M-mono"

"""config = AutoConfig.from_pretrained(
  trust_remote_code=True,
  max_new_tokens=1024
)"""

model = AutoModelForCausalLM.from_pretrained('Salesforce/codegen-350M-mono')
tokenizer = AutoTokenizer.from_pretrained('Salesforce/codegen-350M-mono')

text = """
a = 10

memoization = dict()

def recursive_function(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 3
    
    return recursive_function(a-1) + recursive_function(a-2)

print(recursive_function(a))

'fix this function please fibonacci series'
"""

completion = model.generate(**tokenizer(text, return_tensors="pt"),max_length= 180)

print(tokenizer.decode(completion[0]))

"""steps = 3

for i in range(steps):
        generated_code = mimic_llm_inference(input())
        feedback_code = mimic_llm_feedback(input())"""