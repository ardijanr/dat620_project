import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from accelerate import Accelerator, load_checkpoint_and_dispatch

import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

from huggingface_hub import login

login(token=HF_TOKEN)

model_name = "mistralai/Mistral-7B-v0.3"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    low_cpu_mem_usage=True,
    torch_dtype=torch.float16
)


accelerator = Accelerator()
save_directory="./content/model"
accelerator.save_model(
    model=model,
    save_directory=save_directory,
    max_shard_size="200MB"
)

device_map={"":'cpu'}

model = load_checkpoint_and_dispatch(
    model,
    checkpoint="/content/model/",
    device_map=device_map,
    no_split_module_classes=["Block"]
)

new_model = "sharded_mistral"

tokenizer.push_to_hub(
    new_model,
    token=HF_TOKEN
)

model.push_to_hub(
    new_model,
    token=HF_TOKEN
)



model_name = "mistralai/Mistral-7B-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    low_cpu_mem_usage=True,
    torch_dtype=torch.float16
)

model_name = "something/Mistral-7B-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    low_cpu_mem_usage=True,
    torch_dtype=torch.float16
)