# Text-to-Speech Script

This Python script utilizes the `gtts` library to convert text from a file into speech and save it as an MP3 file. It then plays the generated voice using the default media player on your system.

## Prerequisites
- Python 3.x
- `gtts` library: Install it using `pip install gtts`

## Usage
1. Place the text you want to convert into speech in a file named `abc.txt`. Ensure the file is in the same directory as this script.
2. Run the script using `python script.py`.
3. The script will read the contents of `abc.txt` and generate an MP3 file named `voice.mp3`.
4. The generated voice will be played using the default media player on your system.

## Additional Information
- The `lang` parameter in the `gTTS` function can be modified to specify the language of the generated speech. Currently, it is set to English ('en').
- By default, the speech generation is not slowed down. If you want the speech to be slower, change the `slow` parameter to `True` in the `gTTS` function.
- The line `#print(file)` is commented out. If you want to print the contents of the file to the console, uncomment this line by removing the '#' symbol.

Feel free to customize and adapt this script to suit your needs. Enjoy converting your text into speech!