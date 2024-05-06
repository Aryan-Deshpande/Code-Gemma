from transformers import AutoTokenizer, AutoModelForCausalLM



tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

def mimic_llm_inference(text): # this function inferences an LLM
    pass

    generated_ids = model.generate(input_ids, max_length=128)
    print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))

def mimic_llm_feedback(code):
    input_ids = tokenizer(code, return_tensors="pt").input_ids

    generated_ids = model.generate(input_ids, max_length=128)
    print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))

