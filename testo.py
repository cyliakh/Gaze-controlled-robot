from turtle import left
import cv2 
from cv2 import threshold
from nbformat import write
import numpy as np
import dlib
from math import hypot
import serial
import time
from regex import R


cap = cv2.VideoCapture(0) # this number depends on your camera if it is internal or external
board = np.zeros((200,200), np.uint8)
board [:] = 255
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") # download this + the png file and put them in the same folder as your code

#keyboard stuff 
keyboard = np.zeros((350, 1400, 3), np.uint8)
keyboard [:] = (180, 180, 30)
keys_set_1 = {0: "0", 1: "30", 2: "60", 3: "90", 4: "120", 5: "150", 6: "180"}

list = {0: "Servo", 1: "Grip", 2: "Waist", 3: "Y-ax", 4: "Z-ax"}

serv = "SELECT SERVO"
ecran = np.zeros((200, 200, 3), np.uint8)

w = 200
h = 200
th = 3

def letter(letter_index, text, letter_light):
   w = 200
   h = 150
   th = 3
   if letter_index == 0:
       x = 0
       y = 0
   elif letter_index == 1:
       x = 200
       y = 0
   elif letter_index == 2:
       x = 400
       y = 0
   elif letter_index == 3:
       x = 600
       y = 0
   elif letter_index == 4:
       x = 800
       y = 0
   elif letter_index == 5:
       x = 1000
       y = 0
   elif letter_index == 6:
       x = 1200
       y = 0
   elif letter_index == 7:
       x = 470
       y = 200
       w = 400
       th = 3
       h = 150


   
   if letter_light is True:
       cv2.rectangle(keyboard, (x + th, y + th), (x+ w - th, y + h - th), (210, 255, 255), -1)
   else:
       cv2.rectangle(keyboard, (x + th, y + th), (x+ w - th, y + h - th), (180, 180, 40), th)
   
   cv2.rectangle(keyboard, (x + th, y + th), (x + w - th, y + h - th), (0, 0, 0), th)
   font_letter = cv2.FONT_HERSHEY_SIMPLEX
   font_scale = 3
   font_th = 5
   text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
   #print(text_size)
   width_text, height_text, = text_size[0], text_size[1]
   text_x = int((w - width_text)/2) + x
   text_y = int((h + height_text)/2) + y
   cv2.putText(keyboard,text, (text_x, text_y), font_letter, font_scale, (0, 0, 0), font_th)


def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_SIMPLEX

def get_blinking(eye_points, facial_landmarks):

    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)

    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)    
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))

    ratio = hor_line_length / ver_line_length
    return ratio

def get_gaze_ratio(eye_points, facial_landmarks): 
        left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y), (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y), (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y), (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y), (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y), (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
        height, width, _ = frame.shape
        mask = np.zeros((height, width), np.uint8)
        
        cv2.polylines(mask, [left_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [left_eye_region], 255)
        left_eye = cv2.bitwise_and(gray, gray, mask=mask)

        
        min_x = np.min(left_eye_region[:, 0])
        max_x = np.max(left_eye_region[:, 0])
        min_y = np.min(left_eye_region[:, 1])
        max_y = np.max(left_eye_region[:, 1])
        

        gray_eye = left_eye[min_y: max_y, min_x: max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
        
        height, width, = threshold_eye.shape
        left_side_threshold = threshold_eye[0: height, 0: int(width/2)]
        left_side_white = cv2.countNonZero(left_side_threshold)

        right_side_threshold = threshold_eye[0: height, int(width/2): width]
        right_side_white = cv2.countNonZero(right_side_threshold)

        if left_side_white == 0:
            gaze_ratio = 1
        elif right_side_white == 0:
            gaze_ratio = 5
        else:
            gaze_ratio = left_side_white/right_side_white
        return gaze_ratio

frames = 0
letter_index = 0
blinking_frames = 0
sel = ""
right_frames = 0
left_frames = 0
list_index = 0
side = "LEFT"
last_side = "LEFT"
obj = 0

ser = serial.Serial('COM11', 9600)


while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5)
    keyboard [:] = (180, 220, 40)
    frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    w1 = 1500
    x1 = 0
    y1 = 200
    th1 = 3
    h1  = 150
    cv2.rectangle(keyboard, (x1 + th1, y1 + th1), (x1+ w1 - th1, y1 + h1 - th1), (255, 255, 255), -1)
    cv2.putText(keyboard, serv, (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (150, 190, 40), 7)

    faces = detector(gray)
    for face in faces:

        
        landmarks = predictor(gray, face)

        left_eye_region = np.array([landmarks])

        left_eye_ratio = get_blinking([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2

        
        if gaze_ratio < 0.85:
            ecran [:] = (0, 0, 0)
            cv2.putText(ecran, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
            side = "RIGHT"
            right_frames += 1
            
            if right_frames == 70:
                  time.sleep(2)
                  list_index = list_index + 1
                  ecran[:] = (0, 0, 255)
                  print(list_index)
                  print(list[list_index])
                  serv = list[list_index]
                  if list_index == 1:
                      time.sleep(1)
                      ser.write(b'G')
                      time.sleep(1)
                  elif list_index == 2:
                      time.sleep(1)
                      ser.write(b'W')
                      time.sleep(1)
                  elif list_index == 3:
                      time.sleep(1)
                      ser.write(b'Y')
                      time.sleep(1)
                  elif list_index == 4:
                      time.sleep(1)
                      ser.write(b'Z')
                      time.sleep(1)

                  right_frames = 0
                  ecran [:] = (0, 0, 0)
                  if list_index == 4:
                    list_index = 0             
        else:
            ecran [:] = (0, 0, 0)
            cv2.putText(ecran, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
        
        if blinking_ratio > 7:
            
            blinking_frames += 1
            frames -= 1
            if blinking_frames == 10:
                cv2.putText(frame, "MOUAH", (50, 150), font, 3, (255, 0, 0))
                sel = keys_set_1[letter_index]
                print(letter_index)
                #ser = serial.Serial('COM5', 9600)
                time.sleep(2)
                if letter_index == 0:

                        time.sleep(1)
                        ser.write(b'A')
                        time.sleep(1)

                elif letter_index == 1:
                        time.sleep(1)
                        ser.write(b'B')
                        time.sleep(1)

                elif letter_index == 2:
                        time.sleep(1)
                        ser.write(b'C')
                        time.sleep(1)

                elif letter_index == 3:
                        time.sleep(1)
                        ser.write(b'D')
                        time.sleep(1)

                elif letter_index == 4:
                        time.sleep(1)
                        ser.write(b'E')
                        time.sleep(1)

                elif letter_index == 5:
                        time.sleep(1)
                        ser.write(b'F')
                        time.sleep(1)
                elif letter_index == 6:
                        time.sleep(1)
                        ser.write(b'H')
                        time.sleep(1)

                #ser.close()
                    


        else:
            blinking_frames = 0
        

    if frames == 20:
        letter_index += 1
        frames = 0
        if letter_index == 7:
            letter_index = 0

    for i in range(7):
        letter(i, keys_set_1[i], False)
        letter(letter_index, keys_set_1[letter_index], True)
    cv2.putText(board, sel, (10, 100), font, 2, 0, 3)
    

    cv2.imshow("Frame", frame)
    cv2.imshow("Keyboard", ecran)
    cv2.imshow("Keyb", keyboard)
    cv2.imshow("Board", board)
    key = cv2.waitKey(1)
    if key == 27:
        break
ser.close()

cap.release()

