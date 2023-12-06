# Voice Recording and Speech Recognition

This script allows you to record your voice using a microphone and perform speech recognition on the recorded audio.

## Installation

1. Install the required dependencies:

   ```bash
   pip install SpeechRecognition
   ```

2. Save the script in a file named `voice_recognition.py`.

3. Run the script:

   ```bash
   python voice_recognition.py
   ```

## Usage

1. When you run the script, it will start listening for your voice input.

2. Speak clearly into the microphone.

3. After you finish speaking, the script will attempt to transcribe your speech using Google's speech recognition service.

4. The transcribed text will be saved in a file named `you_said_this.txt`.

5. The script will print a message indicating that the last sentence you spoke has been saved.

## Dependencies

- SpeechRecognition library

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This script utilizes the SpeechRecognition library for speech recognition functionality.
- Special thanks to the SpeechRecognition community for providing the necessary tools for voice recognition.
