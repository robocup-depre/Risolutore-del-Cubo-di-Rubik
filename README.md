# Rubik's cube Solver
This is a Rubik's Cube solver that involves a PC which runs a python script and an AtMega2560 microcontroller installed on a 3D-printed machine that rotates the cube by stepper motors. Each motor is attached to the centre of each face of the cube and can rotate it of 180°, or 90° clockwise/counterclockwise. 

In the "Arduino" folder, you can find the C++ program that has to be flashed into the Arduino board. We have used an Arduino Mega, but even an Arduino Uno can be enough. In fact, you will only need 9 logical pin: one pin controls a relay that connects or disconnects the 12V battery to prevent the motors from vibrating when starting the machine; the DIR pin selects the direction of rotation of the motor; the STEP pin marks the step and six pins (EN1-EN6) enables the driver corresponding to the motor that has to move in a particular instant of time. The STEP and DIR wires are shared between the six driver, but obviously only one motor at time will move, because the Arduino board will enable only one driver at time.
The Arduino program receives the sequence of moves via the serial input fom the PC. Every time it receives a new move, immediatly turns the right motor, and sends a feedback to the PC. 
N.B. Remember to adjust the constant values at the beginning with the number of the pins where you have attached each wire.

In the "Python" folder there are four scripts. To start the resolution process, you have to run the main.py script, that will ask you to write which COM port is the machine connected to.
After that, it will create a GUI with three buttons: clicking the first button you will make the cube scanning process start. To scan the cube you have to place the six faces of the cube in a particular order, that is specified in the "SCANNING_ORDER" image. Pay attention at the order and the orientation of the side facing the camera: if you scan the cube upside-down it won't be solved correctly!
To make this process easyer for the PC even with a medium/low quality webcam, we decided not to make it search for the colors, but for the tags (Apriltags, documentation [here](https://github.com/AprilRobotics/apriltag)).
At the end of the scanning process you will see a two-dimensional representation of the cube. You may check it, and if it's ok you can click the second button, that will calculate the sequence of moves thah solves the cube. During this process the GUi will freeze, and we reccomend not to click anywhere in order to avoid any problems... Now you have to insert the cube like shown in insertion.gif, and finally you can click the last button to start the communication between the PC and the Arduino Board, and that's all!
The other three files are used to execute some tasks like remember the position of each piece after a rotation, or access to the webcam, and so on.
N.B. If you prefer you can use the functions contained in these scrips in your own program, the only thing you have to do is to place these file in the same directory of your script and import them at the beginning of your code). 


Required dependencies:

  -python 3.8;

  -OpenCV(if you prefer using less heavy libraries you can change the code to make it work with pillow/PIL instead of OpenCV);

  -tkinter;

  -winsound;

  -numpy;

  -pupil_apriltags;

  -atmega driver(needed if you cannot recognise which port the machine is connected to).

The machines has been designed with Autodesk Fusion 360 and 3D printed with the printer Sisma Everes Uno. We have mounted it in a wooden base, to hide most wires and the relay. A 12V battery is needed to power the motors, the Arduino board will be powered by the serial cable, so you won't need any other power source except for the 12V battery. We recommend to accurately size the wires, especially those that come out of the battery, in fact each motor can absorb a current of 2A. 
