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


CS = Optical(Ports.PORT20)
brain = Brain()

#to print the color to the screen we need the brain
while True:
    brain.screen.clear_line()
    colour = CS.color()

    msg:str = "Colour: " + str (colour)

    print(msg)
    brain.screen.print_at(msg,x=100,y=100)
    sleep(1)

color = CS.brightness()

brain.screen.print(Color(color))
brain.screen.print(color)
