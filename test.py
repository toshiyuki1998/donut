import re
from transformers import DonutProcessor, VisionEncoderDecoderModel
import torch
from PIL import Image

# models_path = "./models"
models_path = "naver-clova-ix/donut-base-finetuned-cord-v2"

processor = DonutProcessor.from_pretrained(models_path)
model = VisionEncoderDecoderModel.from_pretrained(models_path)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

image = Image.open('/opt/machine_learning/donut/data/invoice.png').convert("RGB")
pixel_values = processor(image, return_tensors="pt").pixel_values

task_prompt = f"<s_code-v2>"

decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids

# output
outputs = model.generate(
    pixel_values.to(device),
    decoder_input_ids=decoder_input_ids.to(device),
    max_length=model.decoder.config.max_position_embeddings,
    pad_token_id=processor.tokenizer.pad_token_id,
    eos_token_id=processor.tokenizer.eos_token_id,
    use_cache=True,
    bad_words_ids=[[processor.tokenizer.unk_token_id]],
    return_dict_in_generate=True,
)

sequence = processor.batch_decode(outputs.sequences)[0]
sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()  # remove first task start token
print(processor.token2json(sequence)["text_sequence"].replace(" ", "\n"))