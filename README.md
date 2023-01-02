# Gaze-controlled-robot

Control a robot through a virtual gaze keyboard using OpenCV with Python.

This project is split on two parts: 

      1- The virtual gaze controlled keyboard.
      
      2- The actual robot to be controlled.

  The keyboard is different depending on the actual robot. If it is a robot arm, the keyboard is divided into two main parts: choosing an angle at which the servo motors of the arm will rotate, and the second part is about choosing which servo motor out of all the motors to control.
  In case of a car instead of robot arm, angles would be replaced by the speed and direction.  
  _ _ _ 

Pre-requisites: 
      
      1- Basic knowledge of object oriented programming in python.
      
      2- Few applications with OpenCV python.
      
      2- Basics and familiarity with microcontrollers.
      
Required libraries:

      1- OpenCV python
      
      2- Numpy, math and time
      
      3- Dlib
      
      4- PySerial 

If you have never worked with OpenCV before, get started with simple Color detection: https://www.youtube.com/watch?v=aFNDh5k3SjU

Also, check the documentation: https://docs.opencv.org/4.x/d9/df8/tutorial_root.html

Python Object Oriented Programming course: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

PySerial tutos: https://www.youtube.com/watch?v=kx4FoOAHG4U&list=PLxob-QD2IjXilpTWXe7eJCI-G-cUbtepE

Python and Arduino communication : https://www.youtube.com/watch?v=OleCp_TAXC8

Arduino serial communication: https://www.youtube.com/watch?v=KYWCkdrCUKg

Numpy tuto for beginners : https://www.youtube.com/watch?v=QUT1VHiLmmI

_____________
      
For the first part of the project which consists of the virtual keyboard: 

First, you will need to detect the eyes in order to track them and detect whenever they blink and detect the direction they are looking at. You will work with **dlib** library and the shape detector of facial landmarks file.
You will also need numpy and math libraries to calculate the distance between the top and the bottom point of the eye and the one between the right corner and left corner of the eye, calculate their ratio to detect the blinking.
You will also need to detect the direction where the eyes are looking at (which is not necessary, depending on your robot as said above, you can skip this part) by calculating the white region inside the eye (choose right or left side of the eye).

Second, you will need to create your keyboard by making an empty frame first, then drawing squares inside it and writing the value/word that each one of them contains.

After finishing this part, a communication between this and the microcontroller is needed. For this part, **PySerial** and **time** libraries is needed. PySerial allows the python code to interact with the microcontroller, and time library is needed to give the required time for the robot to apply and perform the work.
You can either connect your robot directly to your computer so the wire is sufficient for this communication. However, if your robot is movable then in this case you need to add Bluetooth connection. There is another solution which is using **urllib.request** library which allows you to send data to a url instead of a serial communication. 
