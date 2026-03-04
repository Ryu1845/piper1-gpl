"""Needed so package data is included."""

import itertools
from pathlib import Path

from skbuild import setup

MODULE_DIR = Path(__file__).parent / "src" / "piper_phonemize"
PIPER_DATA_FILES = ["py.typed", "espeakbridge.pyi"]
ESPEAK_NG_DATA_DIR = MODULE_DIR / "espeak-ng-data"
ESPEAK_NG_DATA_FILES = [
    f.relative_to(MODULE_DIR) for f in ESPEAK_NG_DATA_DIR.rglob("*") if f.is_file()
]
TASHKEEL_DATA_DIR = MODULE_DIR / "tashkeel"
TASHKEEL_DATA_FILES = [
    (TASHKEEL_DATA_DIR / f_name).relative_to(MODULE_DIR)
    for f_name in (
        "model.onnx",
        "input_id_map.json",
        "target_id_map.json",
        "hint_id_map.json",
    )
]

setup(
    name="piper-phonemize",
    version="2.0.0",
    description="Fast text-to-phoneme conversion using espeak-ng",
    url="http://github.com/OHF-voice/piper1-gpl",
    license="GPL-3.0-or-later",
    author="The Home Assistant Authors",
    author_email="hello@home-assistant.io",
    keywords=["phonemize", "phonemes", "espeak", "tts", "text-to-speech"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.9",
    install_requires=[
        "onnxruntime>=1,<2",
    ],
    extras_require={
        "dev": [
            "pytest>=8,<9",
        ],
        "zh": [
            "g2pW>=0.1.1,<1",
            "sentence-stream>=1.2.1,<2",
            "unicode-rbnf>=2.4.0,<3",
            "torch>=2,<3",
            "requests>=2,<3",
        ],
    },
    packages=["piper_phonemize", "piper_phonemize.tashkeel"],
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "piper_phonemize": [
            str(p)
            for p in itertools.chain(
                PIPER_DATA_FILES, ESPEAK_NG_DATA_FILES, TASHKEEL_DATA_FILES
            )
        ],
    },
    cmake_install_dir="src/piper_phonemize",
)
