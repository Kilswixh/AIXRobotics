# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       final.py                                                      #
# 	Author:       calvin                                                        #
# 	Created:      7/22/2025, 10:35:50 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from time import sleep
from vex import Motor, Ports, TURNS, Optical, Brain,Color,VelocityUnits
from vex import FORWARD, REVERSE
from vex import *
import math

# Elikem's code for line follower

#Declaring constants for my robot specifications.
DEFAULT_SPEED_PCT = 12
DEFAULT_TRACK_WIDTH_CM = 30
DEFAULT_CIRCUMFERENCE_CM = 31.45

#Initializations
colour_sensor = Optical(Ports.PORT20)
left_motor = Motor(Ports.PORT1)
right_motor = Motor(Ports.PORT10)
brain = Brain()


def turn(left_motor, right_motor, angle_deg, speed_pct=DEFAULT_SPEED_PCT,
         track_width_cm=DEFAULT_TRACK_WIDTH_CM, circumference_cm=DEFAULT_CIRCUMFERENCE_CM,
         pivot='left'):
    
    rot = (math.pi * track_width_cm * angle_deg / 180.0) / circumference_cm

    if pivot == 'left':
        left_motor.stop()
        right_motor.spin_for(DirectionType.FORWARD, rot, TURNS, speed_pct, VelocityUnits.PERCENT, True)
    else:
        right_motor.stop()
        left_motor.spin_for(DirectionType.FORWARD, rot, TURNS, speed_pct, VelocityUnits.PERCENT, True)


def calibrate_line(n_samples=10, delay_ms=5000, pause_ms=2000):
    colour_sensor.set_light(LedStateType.ON)
    colour_sensor.set_light(78)
    colour_sensor.set_light_power(78)
    brain.screen.clear_screen()
    brain.screen.print_at("Place on BLACK", x=100, y=100)
    wait(pause_ms, TimeUnits.MSEC)

    black_readings = []
    for i in range(n_samples):
        val = colour_sensor.brightness()
        black_readings.append(val)
        brain.screen.print_at("Black " + str(i + 1) + "/" + str(n_samples) + ": " + str(val), x=100, y=120)
        wait(delay_ms, TimeUnits.MSEC)

    brain.screen.clear_screen()
    brain.screen.print_at("Place on WHITE", x=100, y=100)
    wait(pause_ms, TimeUnits.MSEC)

    white_readings = []
    for i in range(n_samples):
        val = colour_sensor.brightness()
        white_readings.append(val)
        brain.screen.print_at("White " + str(i + 1) + "/" + str(n_samples) + ": " + str(val), x=100, y=120)
        wait(delay_ms, TimeUnits.MSEC)

    black_avg = sum(black_readings) / n_samples
    white_avg = sum(white_readings) / n_samples
    m = 100.0 / (white_avg - black_avg + 1e-6)
    c = -m * black_avg

    brain.screen.clear_screen()
    brain.screen.print_at("Calibration complete", x=100, y=100)
    brain.screen.print_at("m = " + str(m) + ", c = " + str(c), x=100, y=120)
    wait(pause_ms, TimeUnits.MSEC)

    return m, c

def simple_black_white_movement(n_samples=10, delay_ms=50):
    colour_sensor.set_light(100)
    m, c = calibrate_line(n_samples, delay_ms)
    brain.screen.clear_screen()
    brain.screen.print_at("Starting Movement...", x=100, y=100)
    wait(2000, TimeUnits.MSEC)

    while True:
        raw = colour_sensor.brightness()
        calibrated = m * raw + c

        brain.screen.clear_screen()
        brain.screen.print_at("Raw: " + str(raw), x=10, y=20)
        brain.screen.print_at("Cal: " + str(int(calibrated)), x=10, y=40)

        if calibrated < 50:
            brain.screen.print_at("BLACK: turning right", x=10, y=60)
            # turn(left_motor, right_motor, angle_deg=90, speed_pct=DEFAULT_SPEED_PCT, pivot='right')
            # drive(left_motor, right_motor, distance_cm=10, speed_pct=DEFAULT_SPEED_PCT, circumference_cm=DEFAULT_CIRCUMFERENCE_CM)
            turn(left_motor, right_motor, angle_deg=3, speed_pct=DEFAULT_SPEED_PCT, pivot='left')
            
        else:
            brain.screen.print_at("WHITE: turning left", x=10, y=60)
            turn(left_motor, right_motor, angle_deg=3, speed_pct=DEFAULT_SPEED_PCT, pivot='right')

        wait(100, TimeUnits.MSEC)

    # My code for color path