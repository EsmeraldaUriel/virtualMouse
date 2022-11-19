import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()

while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.BGR2RGB)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
