from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize
model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_bn_en")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_bn_en", legacy=False)
input_sentence = "আমার নাম তাহরিম রহমান অনন"
print(input_sentence)
input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
print(input_ids)
input_sentence = "মুহূর্ত"
input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
print(input_ids)
input_sentence = "আপনি যা খুঁজছেন তা আপনাকে খুঁজছে"
input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
print(input_ids)
generated_tokens = model.generate(input_ids)
print(generated_tokens)
decoded_tokens = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
print(decoded_tokens)