
# NMT

This repository contains the code for a machine translation model that translates Bangla text to English using the `banglat5_nmt_bn_en` model from Hugging Face's Transformers library.

## Model Details

- **Model**: `csebuetnlp/banglat5_nmt_bn_en`
- **Tokenizer**: `csebuetnlp/banglat5_nmt_bn_en`

## Dataset

The dataset used is `csebuetnlp/BanglaNMT`, which can be loaded using the Hugging Face `datasets` library.

## Usage

To translate Bangla text to English:

```python
from translator import translate
translation = translate("আপনার বাংলা টেক্সট")
print(translation)
```

## Performance

The translation quality is evaluated using SacreBLEU scores.

## Requirements

- transformers
- datasets
- sacrebleu

## Installation

To install the required libraries:

```shell
pip install transformers datasets sacrebleu
```

## Contributors

- The script is built using Hugging Face's Transformers and Datasets libraries.
- SacreBLEU is used for evaluation.

For more details on the model and its capabilities, please refer to the [Hugging Face Model Card](https://huggingface.co/csebuetnlp/banglat5_nmt_bn_en).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```

Remember to replace the `LICENSE.md` with the actual license text you are using for your project. This README assumes a MIT License, which is common for open-source projects but you should use the license that matches your project's needs.
