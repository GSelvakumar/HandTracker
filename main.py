# Packages used
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Previous and Current time init

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                #print(id, lm)

                # converting decimal placing to pixels

                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                print(id, cx, cy)

                if id == 0:
                    cv2.circle(img, (cx, cy), 16, (255, 0 , 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # show FPS in Ouptut Screen

    cv2.putText(img=img, text="FPS:"+str(int(fps)), org=(10,70), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255, 0, 255), thickness=2)

    cv2.imshow("Image", img) # used to display image in the window
    cv2.waitKey(1) # wait for a pressed key time(ms) if 0 means wait forever shows a second snap. but 1 is responsive live snaps.