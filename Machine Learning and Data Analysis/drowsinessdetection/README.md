# Drowsiness Detection using Computer Vision and Deep Learning

This is a Python script for detecting drowsiness in real-time using computer vision and deep learning techniques. The script uses a pre-trained convolutional neural network (CNN) model to classify the eyes as open or closed, and based on the classification results, it determines the drowsiness level of the person.

## Requirements
To run this script, you need to have the following:

1. Python 3.x
2. OpenCV library (`pip install opencv-python`)
3. Keras library (`pip install keras`)
4. NumPy library (`pip install numpy`)
5. Pygame library (`pip install pygame`)

## How it Works
1. The script uses Haar cascade classifiers to detect faces and eyes in the video frames.
2. It captures video frames from the default camera (index 0) using OpenCV's `VideoCapture` class.
3. For each frame, it detects faces using the face cascade classifier and eyes using the left eye and right eye cascade classifiers.
4. It extracts the eye regions and resizes them to a fixed size (24x24 pixels) for input to the CNN model.
5. The pre-trained CNN model predicts whether the eyes are open or closed based on the input eye images.
6. The script keeps track of the score, which increases when the eyes are closed and decreases when the eyes are open.
7. If the score exceeds a certain threshold (15 in this script), it indicates that the person is feeling sleepy, and an alarm sound is played.
8. The script also draws rectangles and displays text on the video frame to indicate the drowsiness level and score.
9. It continues this process until the user presses the 'q' key to quit the application.

## Usage
1. Make sure you have installed all the required libraries mentioned above.
2. Download the Haar cascade classifier XML files and place them in the "haar cascade files" directory.
3. Put the `alarm.wav` file in the same directory as the script. You can replace it with any sound file of your choice.
4. Run the script using the command `python drowsiness_detection.py`.
5. A window will open showing the video feed from the camera with the drowsiness detection overlays.
6. Press the 'q' key to stop the script.

## GitHub Readme
```markdown
# Drowsiness Detection using Computer Vision and Deep Learning

This repository contains a Python script for real-time drowsiness detection using computer vision and deep learning techniques. It uses a pre-trained convolutional neural network (CNN) to classify the eyes as open or closed, and based on the classification results, it determines the drowsiness level of a person.

## Requirements
To run this script, you need to have the following:

- Python 3.x
- OpenCV library (`pip install opencv-python`)
- Keras library (`pip install keras`)
- NumPy library (`pip install numpy`)
- Pygame library (`pip install pygame`)

## Usage
1. Clone this repository to your local machine.
2. Make sure you have installed all the required libraries mentioned above.
3. Download the Haar cascade classifier XML files and place them in the "haar cascade files" directory.
4. Put the `alarm.wav` file in the same directory as the script. You can replace it with any sound file of your choice.
5. Open a terminal or command prompt and navigate to the directory containing the script.
6. Run the script using the command `python drowsiness_detection.py`.
7. A window will open showing the video feed from the camera with the drowsiness detection overlays.
8. Press the 'q' key to stop the script.

Feel free to customize the script according to your needs or integrate it into your own projects.

## License
This project is licensed under the [MIT License](LICENSE).
