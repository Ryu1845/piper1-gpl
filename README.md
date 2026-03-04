# piper-phonemize

Fast text-to-phoneme conversion using [espeak-ng][].

Converts text to IPA phonemes (and optionally phoneme IDs) for use in speech synthesis pipelines.

## Install

```sh
pip install piper-phonemize
```

## Usage

```python
from piper_phonemize import EspeakPhonemizer, phonemes_to_ids

phonemizer = EspeakPhonemizer()

# Text to phonemes
phonemes = phonemizer.phonemize("en-us", "Hello world")
# [['h', 'ə', 'l', 'ˈ', 'o', 'ʊ', ' ', 'w', 'ˈ', 'ɜ', 'ː', 'l', 'd']]

# Phonemes to IDs
ids = phonemes_to_ids(phonemes[0])
```

## Features

- Fast phonemization via espeak-ng C extension (no subprocess)
- Bundled espeak-ng data (no system install needed)
- Arabic diacritization (tashkeel) built in
- Optional Chinese phonemization (`pip install piper-phonemize[zh]`)
- Phoneme-to-ID mapping for neural TTS models

## License

GPL-3.0-or-later

[![A library from the Open Home Foundation](https://www.openhomefoundation.org/badges/ohf-library.png)](https://www.openhomefoundation.org/)

[espeak-ng]: https://github.com/espeak-ng/espeak-ng
