# Packages used
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow() # used to display image in the window
    cv2.waitKey(1) # wait for a pressed key time(ms) if 0 means wait forever