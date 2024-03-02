from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize
import sacrebleu

#load model
model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_bn_en")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_bn_en", legacy=False)
dataset = load_dataset("csebuetnlp/BanglaNMT")

def translate(text):
input_ids = tokenizer(normalize(text), return_tensors="pt").input_ids
generated_tokens = model.generate(input_ids)
return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

reference = []
candidates = []

for i, example in enumerate(dataset['test']):
    if i % 10 == 0:
        print(f"processing example {i}")
        translation = translate(example['bn'])
        print(translation)
        candidates.append(translation)
        references.append(example['en']) 
sacrebleu_score = sacrebleu.corpus_bleu(candidates, refereneces)
print(f"SacreBLEU score: {sacrebleu_score.score}")
