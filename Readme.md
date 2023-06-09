# Real-Time Multi-Face Recognition

This is a Python application that utilizes the power of face recognition to perform real-time face recognition on live video feeds. The application is built using Python and PyQT, providing an intuitive graphical user interface (GUI) for easy interaction.

## Features

- **Real-time face recognition:** The application is capable of performing face recognition in real-time, allowing for quick and efficient identification of individuals from a live video feed.

- **Multi-face recognition:** The application supports the recognition of multiple faces simultaneously, making it suitable for scenarios where there are multiple individuals present in the video feed.

- **Training capabilities:** The application provides functionality to train the face recognition model with a set of labeled images. This allows for customization and adaptation to different individuals or environments.

- **Graphical User Interface:** The application offers a user-friendly GUI built using PyQT, making it easy to navigate and interact with the various features and settings.

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- PyQT

## Installation

1. Clone the repository:

   ```
   git clone git@github.com:jainil30/Real-Time-Multi-Face-Recognition.git
   ```

2. Install the required Python packages:

   ```
   pip install opencv-python face_recognition PyQt5
   ```

## Usage

1. Run the application:

   ```
   python main.py
   ```

2. The application will launch the GUI, allowing you to perform the following actions:

   - **Train:** Clicking on the "Train" button will open a new window where you can add labeled images for training the face recognition model. Follow the instructions provided to capture images of individuals and provide their corresponding labels.

   - **Recognize:** Clicking on the "Recognize" button will start the real-time face recognition process on the live video feed. Detected faces will be labeled with their corresponding names if recognized.

   - **Settings:** The application provides various settings such as adjusting the confidence threshold for face recognition and selecting the video source (e.g., webcam or pre-recorded video).

   - **Exit:** Clicking on the "Exit" button will close the application.

## Examples

![Add Person Filled Information](GUI%20Screen%20Shots/Add%20Person%20Filled%20Information.png)
*Add Person Filled Information*

![Face Recognition After Camera Started](GUI%20Screen%20Shots/Face%20Recognition%20After%20Camera%20Started.png)
*Face Recognition After Camera Started*

<!-- ## User Guide

[Download User Guide](Images/UserGuide/user_guide.pdf)

The user guide provides detailed instructions on how to use the application, along with explanations of various features and settings.
 -->
Here are a few examples of how to use the application:

- Training the model:
  1. Click on the "Train" button.
  2. Follow the instructions to capture images and provide labels for training.
  3. Click on the "Train" button to start the training process.
  4. Once the training is complete, close the training window.

- Performing real-time face recognition:
  1. Click on the "Recognize" button.
  2. The application will start detecting and recognizing faces in the live video feed.
  3. Recognized faces will be labeled with their corresponding names.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [face_recognition](https://github.com/ageitgey/face_recognition): The face recognition library used in this project.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact [Jainil Dalwadi](mailto:your-email@example.com).

## Disclaimer

**Note:** This project was developed as part of a college project or assignment. While it showcases the implementation of real-time multi-face recognition using Python and PyQT, please be aware that it may have limitations or areas for improvement.

We acknowledge that this project can be enhanced in various ways, such as improving accuracy, optimizing performance, and refining the user interface. Although the project may not be actively maintained or updated, it serves as a demonstration of our skills and knowledge during its development.

We encourage developers and enthusiasts to explore, build upon, and enhance this project further. Contributions, suggestions, and improvements are always welcome.
