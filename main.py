import cv2
import time
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands=2,detectionCon=0.8)
from pynput.keyboard import Key, Controller
keyboard=Controller()

cap=cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
while True:
    success,img=cap.read()
    hand,img=detector.findHands(img)
    if hand:
        hand1=hand[0]     
        if hand1['type']=='Right':
              keyboard.release(Key.left)
              keyboard.press(Key.right)
        if hand1['type']=='Left':
              keyboard.release(Key.right)
              keyboard.press(Key.left)     
            
    cv2.imshow("Success",img)
    cv2.waitKey(1)