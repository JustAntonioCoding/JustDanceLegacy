# Just Antonio's Just Dance Legacy Tools
Public repository of my tools for Just Dance modding

## Description for each tool
### audioCutterJDU
Put `*codename*_musictrack.tpl.ckd` and `*codename*.ogg` in folder `input`<br>
You'll get `*codename*.ogg` and `amb_*codename*_intro.ogg` in folder `output`<br>
Prerequisite to run:<br>
[`FFMPEG`](https://ffmpeg.org)

### avatarMaker
Put already converted avatar textures named like `*codename*_*avatarNumber*.png.ckd` or `*avatarNumber*.png.ckd` in folder `input`<br>
Make sure to backup your avatar textures, because they are renamed and moved to folder `output`<br>

### bkgGenMshMaker
Input colors as RGB values

### ipkUnpacker
This tool unpack all *.ipk files in current folder<br>
It also can pack all folder to *.ipk format by using folder names<br>
Final output is named `*folderName*_*console*.ipk`<br>
Make sure to edit start of `ipkPacker.py` to change console variable

## Bugs and suggestions
Let me know if you have suggestions for any improvements for these tools or idea for creating new ones<br>
If you use them make sure to credit me :blue_heart:	
