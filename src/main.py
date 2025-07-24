# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       calvin                                                        #
# 	Created:      7/22/2025, 10:35:50 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       color.py                                                      #
# 	Author:       calvin                                                        #
# 	Created:      7/22/2025, 10:35:50 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from time import sleep
from vex import Motor, Ports, TURNS, Optical, Brain,Color
from vex import FORWARD, REVERSE
from vex import *

#declaring motor ports
right_motor = Motor(Ports.PORT1,True)
left_motor = Motor(Ports.PORT10)

#declaring optical ports
CS = Optical(Ports.PORT20)


brain = Brain()
buffer_Y:float = 10
buffer_B:float = 10
buffer_W:float = 10
buffer_P:float = 10
buffer:float = 4.3
buffer:float = 4.3
buffer:float = 4.3


# to spin right a degree specific for my robot
def spin_a_degreeR(degree,velocity):
    n = (degree *30)/5
    n= n/2
    right_motor.spin_for(REVERSE,n,velocity = velocity,wait=False)
    left_motor.spin_for(FORWARD,n,velocity = velocity)

# to turn right a degree specific for my robot
def turn_a_degreeR(degree,velocity):
    n = (degree * 30)/5
    right_motor.spin_for(REVERSE,n,velocity = velocity,wait=False)
    left_motor.spin_for(FORWARD,n,velocity = velocity)


# to spin left a degree specific for my robot
def spin_a_degree(degree,velocity):
    n = (degree *30)/5
    n= n/2
    right_motor.spin_for(FORWARD,n,velocity = velocity,wait=False)
    left_motor.spin_for(REVERSE,n,velocity = velocity)

# to turn left a degree specific for my robot
def turn_a_degree(degree,velocity):
    n = (degree * 30)/5
    right_motor.spin_for(FORWARD,n,velocity = velocity,wait=False)
    left_motor.spin_for(REVERSE,n,velocity = velocity)
# to move in a straight line

def move_straight(distance,velocity):
    circumferance = 31.45
    distance = distance/circumferance
    right_motor.spin_for(FORWARD,distance,TURNS,velocity = velocity, wait= False)
    left_motor.spin_for(FORWARD,distance,TURNS,velocity = velocity)


def function_Orange():
    #to print the color to the screen we need the brain
    move_straight(29.6*2.2,20)
     


def function_Green():
    move_straight(29.6,20)
    
def function_Red():
    move_straight(29/2,20)
    right_motor.stop()
    left_motor.stop()


def function_White():
    move_straight(29.6,20)
        


def function_Pink():
    spin_a_degree(180,20)
    move_straight(29.6,20)
        


def function_Blue():
    spin_a_degree(90,20)
    move_straight(29.6,20)


def function_Yellow():
    spin_a_degreeR(90,20)
    move_straight(29.6,20)

Orange_C = 1.29
Orange_H = 20

Green_C = 0.26
Green_H = 153

White_C = 1
White_H = 180

Pink_C = 0
Pink_H = 350

Blue_C = 0.22
Blue_H = 240

Yellow_C = 1.59
Yellow_H = 70

Red_C = 0
Red_H = 12



while True:
    brain.screen.clear_screen()
    colour = CS.brightness()
    colour2 = CS.hue()

    # Orange works
    if Orange_C-buffer<=colour<=Orange_C+buffer and Orange_H-buffer<=colour2<=Orange_H+buffer:
        brain.screen.print_at("Orange",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_Orange()
        wait(1000)


    if Green_C-buffer<=colour<=Green_C+buffer and Green_H-buffer<=colour2<=Green_H+buffer:
        brain.screen.print_at("Green",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_Green()
        wait(1000)

    if Red_C-buffer<=colour<=Red_C+buffer and Red_H-buffer<=colour2<=Red_H+buffer:
        brain.screen.print_at("Red",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_Red()
        wait(1000)
        break

    if White_C-buffer<=colour<=White_C+buffer and White_H-buffer_W<=colour2<=White_H+buffer_W:
        brain.screen.print_at("White",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_White()
        wait(1000)

    if Pink_C-buffer<=colour<=Pink_C+buffer and Pink_H-buffer<=colour2<=Pink_H+buffer:
        brain.screen.print_at("Pink",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_Pink()
        wait(1000)

    if Blue_C-buffer<=colour<=Blue_C+buffer and Blue_H-buffer_B<=colour2<=Blue_H+buffer_B:
        brain.screen.print_at("Blue",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_Blue()
        wait(1000)

    if Yellow_C-buffer<=colour<=Yellow_C+buffer and Yellow_H-buffer_Y<=colour2<=Yellow_H+buffer_Y:
        brain.screen.print_at("Yellow",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        function_Yellow()
        wait(1000)

    else:
        brain.screen.print_at("UNKNOWN",x=90,y=70)
        brain.screen.print_at(CS.brightness(),x=90,y=100)
        brain.screen.print_at(CS.hue(),x=90,y=120)
        wait(1000)
