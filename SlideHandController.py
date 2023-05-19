import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
from pynput.keyboard import Key, Controller

keyboard = Controller()  # Simulating Keyboard Inputss

detector = htm.HandsDetector()

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
flag = ''

thres = 15  # --> change it if any problem (Decrease if small hands, Increase if big hands)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # time.sleep(2)
    temp = flag
    flag = detector.direction_hand(img, thres, 12, 0, flag)
    left_or_right_hand = detector.left_or_right(img)

    #### if hand is pointing up and the last input was not up ####
    # if flag == 'u' and temp != flag:
    #     # keyboard.press(Key.up)
    #     # keyboard.release(Key.up)
    #     print("u")
    
    # #### if hand is pointing down and the last input was not down ####
    # # elif flag == 'd' and temp != flag:
    # #     keyboard.press(Key.down)
    # #     keyboard.release(Key.down)
    # #     print("d")

    # #### if hand is pointing right and the last input was not right (IMAGE IS FLIPPED!!!!) ####
    # elif flag == 'l' and temp != flag:
    #     keyboard.press(Key.right)
    #     keyboard.release(Key.right)
    #     print("l")

    # #### if hand is pointing left and the last input was not left (IMAGE IS FLIPPED!!!!) ####
    # elif flag == 'r' and temp != flag:
    #     keyboard.press(Key.left)
    #     keyboard.release(Key.left)
    #     print("r")

    if flag == 'dull' and temp != flag:
        # keyboard.press(Key.up)
        # keyboard.release(Key.up)
        print("u")

    elif flag == 'action' and temp != flag and left_or_right_hand == 'lh':
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        print("l")

    elif flag == 'action' and temp != flag and left_or_right_hand == 'rh':
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        print("r")

    #### fps calculations (Greater the better) ####
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()