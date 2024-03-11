import torch

from trl import SFTTrainer
from datasets import load_dataset
from peft import LoraConfig, PeftModel, prepare_model_for_kbit_training, get_peft_model

from transformers import TrainingArguments
from transformers import AutoModelForCausalLM, AutoTokenizer

dataset = load_dataset("sahil2801/CodeAlpaca-20k",split="train")

model = AutoModelForCausalLM.from_pretrained("mmukh/SOBertBase")
tokenizer = AutoTokenizer.from_pretrained("mmukh/SOBertBase")
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
tokenizer.pad_token = '[PAD]'
tokenizer.padding_side = "right"

peft_config = LoraConfig(

    r=32,
    lora_alpha=64,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules="all-linear"
)

model = get_peft_model(model, peft_config)

training_arguments = TrainingArguments(
        output_dir="content/results",
        num_train_epochs=10,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=32,
        logging_steps=25,
        optim="paged_adamw_8bit",
        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_steps=10,
        warmup_ratio=0.05,
        weight_decay=0.01,
        max_steps=-1,
)

trainer = SFTTrainer(
    model,
    train_dataset=dataset,
    dataset_text_field="instruction",
    peft_config=peft_config,
    max_seq_length=512,
    tokenizer=tokenizer
)

trainer.train()