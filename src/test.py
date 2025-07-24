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
    colour = CS.brightness()
    CS.set_light_power(50)
    msg:str = "Colour: " + str (colour)
   
    print(msg)
    brain.screen.print_at(msg,x=100,y=70)
    brain.screen.print_at("Bri: " + str(CS.brightness()),x=100,y=90)
    brain.screen.print_at("hue: " + str(CS.hue()),x=100,y=110)
    brain.screen.print_at("rgb: " + str(CS.rgb()),x=100,y=130)
    sleep(1)

