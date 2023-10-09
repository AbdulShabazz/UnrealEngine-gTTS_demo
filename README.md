# UnrealEngine-gTTS_demo
An offline Google text-to-speech library and respeecher voice-mapping tool for Unreal Engine 5, powered by Python 3.11.

An internet connection is required.

Ensure pip is up to date before installing gTTS.

### ensurepip

Python comes with an `ensurepip` module, which can install pip from a Python environment.

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

### numpy

Numpy (16MB) is a python library used in scientific computing.

```{pip-cli}
$ pip install numpy
```
or
```{pip-cli}
$ python.exe -m pip install numpy
```

### pydub

Pydub (32KB) is a python library which converts between audio file formats.

```{pip-cli}
$ pip install pydub
```
or
```{pip-cli}
$ python.exe -m pip install pydub
```

Module:
```python
>>> import pydub
>>> # Load the FLAC audio file
>>> input_audio = pydub.AudioSegment.from_file('input.flac', format='flac')
>>> # Convert the FLAC audio to WAV format.
>>> output_audio = input_audio.export('output.wav', format='wav')
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

### Other recommended libraries

[ffmpeg](https://ffmpeg.org/download.html) - For converting between audio and video files, extracting audio from video files, generating thumbnails, and transcoding-, splitting-, merging- audio and video files.
[avconv](https://ffmpeg.org/download.html) - For converting between audio and video files, extracting audio from video files, generating thumbnails, and transcoding-, splitting-, merging- audio and video files. Now part of the ffmpeg python library. Refer to the How-To-Use documentation.

### ffmpeg-python

```{pip-cli}
$ pip install ffmpeg-python
```
or
```{pip-cli}
python.exe -m pip install ffmpeg-python
```

Module:
```python
>>> import ffmpeg
>>> # Load the input video file
>>> input_video = ffmpeg.input('input.mp4')
>>> # Convert the input video to WEBM format.
>>> output_video = ffmpeg.output(input_video, 'output.webm', format='webm')
>>> # Run the ffmpeg command to convert the video
>>> ffmpeg.run(output_video)
```
