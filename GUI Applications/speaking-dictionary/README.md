# Speaking Dictionary

This script allows you to find the meaning of a word by speaking it out loud. It uses speech recognition to capture your voice input and then uses the PyDictionary library to retrieve the meaning of the word.

## Prerequisites

- Python 3.x
- pyttsx3 library
- PyDictionary library
- speech_recognition library
- gtts library

## Installation

1. Clone the repository or download the script file.
2. Make sure you have Python installed on your system.
3. Install the required libraries by running the following command:

   ```
   pip install pyttsx3 PyDictionary SpeechRecognition gTTS
   ```

## Usage

1. Open the script in a Python IDE or text editor.
2. Run the script.
3. The script will prompt you to say "Hello" to initiate the speaking dictionary.
4. Speak "Hello" into your microphone.
5. The script will ask you to speak the word for which you want to find the meaning. Speak slowly and clearly.
6. The script will capture your voice input and attempt to recognize the word using Google's speech recognition service.
7. If the recognized word is correct, the script will retrieve the meaning of the word using the PyDictionary library and display it on the console.
8. The script will also speak out the meaning of the word using the pyttsx3 library.
9. If the recognized word is incorrect, the script will ask you to try again.
10. You can continue using the speaking dictionary by speaking new words and getting their meanings.

## Note

- Make sure you have a working microphone connected to your computer.
- Ensure that your microphone is properly configured and recognized by your operating system.

## License

This project is licensed under the [MIT License](LICENSE).