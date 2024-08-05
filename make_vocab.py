import json
from transformers import BertTokenizer

model_name = "tohoku-nlp/bert-base-japanese-v3"
base_tokenizer_path = "/opt/machine_learning/donut/data/models/tokenizer.json"
tokenizer_path = "tokenizer.json"

tokenizer = BertTokenizer.from_pretrained(model_name)

vocab = tokenizer.get_vocab()
sorted_vocab = sorted(vocab.items(), key=lambda item: item[1])

with open(base_tokenizer_path, "rb") as f:
    base = json.load(f)

base["model"]["vocab"] += [[token, 0.0] for token, idx in sorted_vocab]

with open(tokenizer_path, "w", encoding="utf-8") as f:
    json.dump(base, f, ensure_ascii=False, indent=2)
