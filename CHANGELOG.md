# Changelog

## 2.0.3 - 2026-07-11

### Fixed

- Chinese phonemizer: load g2pW batches in the main process instead of
  torch DataLoader worker subprocesses, which were slow to start and
  lingered after exit (hanging CI jobs on macOS)

## 2.0.2 - 2026-07-11

### Fixed

- `zh` extra: pin `numpy<2` on Intel macOS, where torch wheels stopped at
  2.2.2 (built against NumPy 1.x) and `tensor.numpy()` fails under NumPy 2

## 2.0.1 - 2026-07-11

### Fixed

- CI: tests now run on every push to `main` and use a non-editable
  install so the espeakbridge extension is actually built
- Release pipeline: skip the Chinese phonemizer test on Windows
  (g2pW does not work there); other platforms still run it

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
