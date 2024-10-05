# Facial Recognition Attendance System

### Overview

This project is a real-time facial recognition attendance system that uses OpenCV, dlib, and the face_recognition library to detect, identify, and log attendance. The system captures video from a webcam, compares detected faces with known encodings, and logs attendance with a timestamp.

---

### Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Known Issues](#known-issues)
8. [Contributing](#contributing)
9. [License](#license)

---

### Features

- **Real-time Face Detection**: Uses a webcam to detect faces in real-time.
- **Face Recognition**: Matches detected faces with stored images and encodings.
- **Attendance Logging**: Automatically logs the name, registration number, and timestamp of recognized individuals into a CSV file.
- **Unrecognized Faces**: Marks unidentified faces as "Intruder."
- **Scalable**: Easily add new images of authorized individuals by placing them in the specified folder.

---

### Project Structure

 ```plaintext
 FacialRecognitionAttendanceSystem/
 │
 ├── ImagesAttendence/        # Folder containing images of authorized individuals
 │   ├── JohnDoe_12345.jpg
 │   ├── JaneSmith_67890.jpg
 │   ├── AliceJohnson_54321.jpg
 │   └── BobBrown_98765.jpg
 │
 ├── attendence.csv           # CSV file to log attendance
 │
 ├── your_script.py           # The main Python script
 │
 ├── requirements.txt         # Dependencies for the project
 │
 └── README.md                # Project documentation
```
---
### Requirements
#### The following libraries and tools are required to run the project:
- Python 3.6 or above
- numpy
- opencv-python
- dlib
- face_recognition

---

### Installation
1. **Clone the repository:**
 ``` bash
 https://github.com/apexwild534/Facial-Recognition-AttendanceSystem.git
 cd Facial-Recognition-AttendanceSystem
 ```
2. **Install required dependencies:**
 ``` bash
pip install -r requirements.txt
 ```
---
### Usage
Once you have all the dependencies installed and your images are ready, you can start the attendance system by running the main Python script:
 ``` bash
python attendence.py
 ```
The script will access the webcam, detect faces, and log attendance in attendence.csv.

#### Adding New Individuals:
To add new authorized individuals:

1. Place their image in the ImagesAttendence/ folder. 
2. The image name should follow this format: Name_RegistrationNumber.jpg (e.g., JohnDoe_12345.jpg).
3. The system will automatically pick up the new person and recognize them during attendance.

---
### Configuration
You can modify the behavior of the system by tweaking certain sections of the code:
- **Attendance CSV**: The system logs attendance in attendence.csv. If you wish to change the output file location, modify the markAttendance() function.
- **Image Resize**: By default, the system scales down the captured frames for performance. If you want to increase or decrease the frame size, change this line:
 ``` python
imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
 ```
---
### Known Issues
- **dlib Installation**: Installing dlib can be difficult on some operating systems, especially Windows. Make sure to follow the installation instructions carefully or use precompiled binaries if necessary.
- **Face Encoding Errors**: If no face is detected in an image, the system may throw an error. Ensure that the input images in ImagesAttendence/ are clear and correctly formatted.
---
### Contributing
 Contributions are always welcome! If you'd like to improve this project, follow these steps:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add a new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.\

Please make sure your code is well-documented and tested before submitting.

---
### License
This project is licensed under the *MIT License*. See the [LICENSE](mit-license) file for more details.

