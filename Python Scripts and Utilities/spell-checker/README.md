# Spelling Correction Script

This script uses the TextBlob library to correct the spelling of a word entered by the user. It continuously prompts the user to enter a word and displays the original text along with the corrected version.

## Prerequisites

Before running this script, make sure you have the following installed:

- Python
- TextBlob library (`pip install textblob`)

## Usage

To use this script, follow these steps:

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script with the following command:

   ```
   python spelling_correction_script.py
   ```

4. The script will prompt you to enter a word to be checked for spelling errors.
5. After entering the word, the script will display the original text and the corrected text.
6. You can choose to try again by entering `1` or exit the script by entering `0`.

## Example

Here's an example of how to use the script:

```
Enter the word to be checked: Helloo
Original text: Helloo
Corrected text: Hello
Try Again? 1 : 0 1
Enter the word to be checked: Wrold
Original text: Wrold
Corrected text: World
Try Again? 1 : 0 0
```

In this example, the script corrects the spelling of the words "Helloo" and "Wrold" to "Hello" and "World" respectively.

## Troubleshooting

If you encounter any issues while running the script, ensure that you have the correct version of Python and the TextBlob library installed. Additionally, make sure you have proper input handling in place to avoid unexpected errors.

If you have any further questions or need assistance, please feel free to open an issue in this repository.