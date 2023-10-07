# UnrealEngine-gTTS_demo
An offline Google text-to-speech library and respeecher voice-mapping tool for Unreal Engine 5, powered by Python 3.11.

An internet connection is required for this library.

Ensure pip is up to date before installing gTTS.

### ensurepip

Python comes with an `ensurepip` module, which can install pip in a Python environment.

```{pip-cli}
$ python -m ensurepip --upgrade
```

### upgrade pip

Also, to upgrade pip at the command line.

```{pip-cli}
$ pip install --upgrade pip
```
or
```{pip-cli}
$ python.exe -m pip install --upgrade pip
```

### gTTS Installation

```{pip-cli}
$ pip install gTTS
```
or
```{pip-cli}
python.exe -m pip install gTTS
```

## Features

-   Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
-   Customizable text pre-processors which can, for example, provide pronunciation corrections;

### Quickstart

Module:
```python
>>> from gtts import gTTS
>>> tts = gTTS('hello')
>>> tts.save('hello.mp3')
```

Optional Command Line:

```{pip-cli}
$ gtts-cli 'hello' --output hello.mp3
```

See <http://gtts.readthedocs.org/> for documentation and examples.

### Disclaimer

This project is *not* affiliated with Google or Google Cloud. Breaking upstream changes *can* occur without prior notice. This project is leveraging the undocumented [Google Translate](https://translate.google.com) speech functionality and is *unrelated* to [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).
