# 🚀 Real-Time Drowsiness Detection System

This project is a Computer Vision application designed to detect eye fatigue.Using Python and facial landmark detection, the system monitors a user's eyes in real-time and triggers an alarm if they remain closed for a specified duration.

## ✨ Key Features
 **Real-Time Detection**: Uses webcam feed for instant analysis.
 **Facial Landmark Mapping:** Utilizes the `dlib` 68-point facial landmark predictor.
 **Eye Aspect Ratio (EAR):** Employs a mathematical formula to calculate the "openness" of the eye.
 **Audio Alerts:** Integrated with `pygame` to sound an alarm when drowsiness is detected.

## 🧠 How It Works
The system captures the video feed and converts it to grayscale. It then:
1. Locates the face in the frame.
2. Identifies the coordinates for the left and right eyes.
3. Calculates the **Eye Aspect Ratio (EAR)**:
   > If the EAR falls below a threshold (e.g., 0.25) for a certain number of frames, the system identifies the user as drowsy and sounds the alarm.

## 🛠️ Tech Stack
 **Language:** Python 3.x
 **Libraries:** OpenCV, Dlib, Scipy, Imutils, Pygame

## 🚀 Installation & Usage
1. **Clone the repository:**
      pip install opencv-python dlib scipy imutils pygame
## 📁 Modal File
      shape_predictor_68_face_landmarks.dat
      you can download it from this link:  https://dlib.net/files/ 
## 🔐Privacy
  ## No Recording: The camera feed is processed frame-by-frame and is never saved or transmitted.
  ## Safety First: This is an educational prototype and should not be used in actual vehicles.
