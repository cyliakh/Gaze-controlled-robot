# Gaze-controlled-robot

Control a robot through a virtual gaze keyboard using OpenCV with Python.

This project is split on two parts: 

      1- The virtual gaze controlled keyboard.
      
      2- The actual robot to be controlled.

  The keyboard is different depending on the actual robot. In this example, we got a robot arm of 4 DOF. So, the keyboard is divided into two main parts: choosing an angle at which the servo motors will rotate, and the second part is about choosing which servo motor out of all the 4 motors to control.
  In case of a car instead of robot arm, angles would be replaced by the speed and direction. 

Pre-requisites: 
      
      1- Basic knowledge of object oriented programming in python.
      
      2- Few applications with OpenCV python.
      
      2- Basics and familiarity with microcontrollers.
      
Required libraries:

      1- OpenCV python
      
      2- Numpy, math and time
      
      3- Dlib
      
      4- PySerial (this is not mandatory, depending on the application)

If you have never worked with OpenCV before, get started with simple Color detection: https://www.youtube.com/watch?v=aFNDh5k3SjU

Also, check the documentation: https://docs.opencv.org/4.x/d9/df8/tutorial_root.html
      
For the first part of the project which consists of the virtual keyboard: 

First, you will need to detect the eyes in order to track them and detect whenever they blink and detect the direction they are looking at. You will work with dlib library and the shape detector of landmarks file.
You will also need numpy and math libraries to calculate the distance between the top and the bottom point of the eye and the one between the right corner and left corner of the eye, calculate their ratio to detect the blinking.
You will also need to detect the direction where the eyes are looking at (which is not necessary, depending on your robot as said above, you can skip this part) by calculating the white region inside the eye (choose right or left side of the eye).

Second, you will need to create your keyboard by making an empty frame first, then drawing squares inside it and writing the value/word that each one of them contains.

After finishing this part, a communication between this and the microcontroller is needed. For this part, PySerial and time libraries is needed. PySerial allows the python code to interact with the microcontroller, and time library is needed to give the required time for the robot to apply and perform the work.
You can either connect your robot directly to your computer so the wire is sufficient for this communication. However, if your robot is movable then in this case you need to add Bluetooth connection. There is another solution which is using urllib.request library which allows you to send data to a url instead of a serial communication. 
