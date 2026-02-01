import cv2 # Camera
import dlib # Face Logic
from scipy.spatial import distance # Math
from imutils import face_utils # Helper for coordinates
import pygame # To play the sound

# 1. Initialize Sound
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("alarm.wav")

# 2. Load the pre-trained 'Brain' files
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 3. EAR Formula (The math that detects closed eyes)
def get_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# 4. Start the Webcam
cap = cv2.VideoCapture(0)
closed_frames = 0 # Counter for how long eyes are closed

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Easier for AI to read
    faces = detector(gray)

    for face in faces:
        # Find 68 dots on the face
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # Eye points: Left [36-42], Right [42-48]
        leftEye = shape[36:42]
        rightEye = shape[42:48]

        # Calculate 'Openness' for both eyes
        ear = (get_ear(leftEye) + get_ear(rightEye)) / 2.0

        # Logic: If EAR is low, eyes are closed
        if ear < 0.25:
            closed_frames += 1
            if closed_frames >= 20: # If closed for ~1 second
                cv2.putText(frame, "DROWSY ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                alarm_sound.play()
        else:
            closed_frames = 0
            alarm_sound.stop()

    cv2.imshow("Drowsiness Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to stop
        break

cap.release()
cv2.destroyAllWindows()