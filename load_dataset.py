from datasets import load_dataset
dataset = load_dataset("csebuetnlp/BanglaNMT")
print(dataset)
dataset['test'][0]
input_sentence = dataset['test'][0]['bn']
input_sentence
reference = dataset['test'][0]['en']
reference
input_sentence = dataset['test'][1]['bn']
input_sentence
reference = dataset['test'][1]['en']
reference