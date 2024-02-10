from transformers import AutoTokenizer
import json

tokenizer = AutoTokenizer.from_pretrained("gpt2")

# printing its tokenization library
# with open("tokenizer.json", "w") as f:
#     json.dump(tokenizer.get_vocab(), f, indent=4)

# get token ids for texts
text = "Hello, I live in the multiverse and I am an ALchemist"
tokens = tokenizer.encode(text)
print(tokenizer.convert_ids_to_tokens(tokens))
print(tokenizer.decode(tokens))
print(tokens)