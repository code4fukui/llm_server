import torch
from transformers import AutoTokenizer
from auto_gptq import AutoGPTQForCausalLM
 
tokenizer = AutoTokenizer.from_pretrained("rinna/youri-7b-chat-gptq")
model = AutoGPTQForCausalLM.from_quantized("rinna/youri-7b-chat-gptq", use_safetensors=True)

def generate_reply(prompt: str) -> str:
    token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
    with torch.no_grad():
        output_ids = model.generate(
            input_ids=token_ids.to(model.device),
            max_new_tokens=200,
            do_sample=True,
            temperature=0.5,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )
    output = tokenizer.decode(output_ids.tolist()[0])
    output = output[len(prompt):-len("</s>")].strip()
    return output
