## Script Usage Instructions

This script generates and verifies CAPTCHA images using the `captcha` library in Python. Follow the steps below to use the script:

### Prerequisites
- Install the `captcha` library by running the following command:
  ```
  pip install captcha
  ```

### Font Setup
1. Download the required fonts to generate CAPTCHA images. The script currently expects two font files:
   - `ChelseaMarketsr.ttf`
   - `DejaVuSanssr.ttf`
   
2. Update the font paths in the script code with the correct paths to the downloaded font files. Locate the following lines in the script:
   ```python
   image = ImageCaptcha(fonts=['C:/Users/Administrator/Downloads/ChelseaMarketsr.ttf', 'C:/Users/Administrator/Downloads/DejaVuSanssr.ttf'])
   ```

   Replace `'C:/Users/Administrator/Downloads/ChelseaMarketsr.ttf'` and `'C:/Users/Administrator/Downloads/DejaVuSanssr.ttf'` with the actual paths to the downloaded font files on your system.

### Running the Script
1. Run the script using a Python interpreter.
2. The script will generate a random CAPTCHA value and save the corresponding image as `out.png`.
3. A window will appear containing the generated CAPTCHA image, along with an input field and two buttons.
4. Enter the CAPTCHA value shown in the image into the input field.
5. Click the "Submit" button to verify the entered value.
6. If the entered value matches the generated CAPTCHA, a success message will be displayed.
7. If the entered value does not match the generated CAPTCHA, an alert message will be displayed, and a new CAPTCHA image will be generated.
8. To generate a new CAPTCHA image without verifying the current value, click the "Refresh" button.

Note: Make sure to have the required fonts installed and correctly specified in the code for the script to work properly.
