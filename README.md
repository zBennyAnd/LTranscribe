# LTranscribe
<br />
<div align="center">
  <a href="https://github.com/zBennyAnd/LTranscribe">
    <img src="logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Ltranscribe</h3>

  <p align="center">
    Transcribe your audios!
    <br />
    <br />
    ·
    <a href="https://github.com/zBennyAnd/LTranscribe/issues">Report Bug</a>
    ·
    <a href="https://github.com/zBennyAnd/LTranscribe/issues">Request Feature</a>
  </p>
</div>

## Description
Recorded lession? Do you have to take notes of long audio?

LTranscribe is a vlc based media player created to help you while transcribing notes from audio.

## How it works?
1) Open your audio file and your favourite text editor
2) Start transcribing!

LTranscribe will stop the audio as soon as you start typing and restart it when you stop.

## Requirements 

### Python Modules
- Some python modules are needed to be installed to run launcher.py file. Before running it be sure to have installed:

  - CustomTkinter
  - python-vlc
  - keyboard
  - Pillow

To install these modules run following commands:
```bash
pip install customtkinter
pip install python-vlc
pip install keyboard
pip install pillow
```
### Software
In order to use LTranscribe _it's necessary to have installed VLC Software __64 bit__ version_.

#### Why?
VLC is used as base for the media player. So it's necessary to run the software.


## Installation
### Windows
On Windows you can download _LTranscribe_vx.y.z_Windows.zip_ from releases, extract it and launch the __shortcut__ to launcher.exe
### Linux/MacOS (Also alternative for Windows)
Download zip file and simply __run launcher.py__

## Usage
### Shortcuts:
- Left arrow: skip 5 seconds
- Right arrow: back 5 seconds
- Use the switch on the left to enable or disable _pause on typing_
## Roadmap
 - [ ] Shortcuts when minimized
 - [ ] Better video support
 - [ ] Add integrated text editor


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU GPLv3](COPYING)