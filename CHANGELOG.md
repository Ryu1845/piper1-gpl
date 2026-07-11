# Changelog

## 2.0.0 - 2026-07-11

Complete rewrite of the project as **piper-phonemize**, a text-to-phoneme
conversion library. The full TTS engine has been stripped down to the
phonemization layer only.

### Changed

- Renamed package from `piper-tts` to `piper-phonemize`
- Moved Python package from `piper` to `piper_phonemize`
- Tests now run on every push to `main`

### Removed

- Neural synthesis and ONNX voice loading
- HTTP server and CLI
- Voice downloading
- Training infrastructure
- C++ library
- PyPI publishing (releases are GitHub-only)

### Retained

- Fast phonemization via the espeak-ng C extension (no subprocess)
- Bundled espeak-ng data (no system install needed)
- Arabic diacritization (tashkeel)
- Optional Chinese phonemization (`piper-phonemize[zh]`)
- Phoneme-to-ID mapping for neural TTS models
