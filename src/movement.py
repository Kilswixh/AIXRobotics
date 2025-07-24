# Library imports
from vex import Motor, Ports, TURNS, Optical, Brain,Color
from vex import FORWARD, REVERSE,VelocityUnits #I am not sure about the velocity unit.
#import movement

#declaring motor ports
right_motor = Motor(Ports.PORT1,True)
left_motor = Motor(Ports.PORT10)

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

# to draw a Square
def draw_Square(distance, degree, speed,speed2):
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)

# to draw a hexagon
def draw_hexagon(distance, degree, speed,speed2):
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)    
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
    move_straight(distance,speed)
    spin_a_degree(degree,speed2)
#draw_hexagon(30,60,19,28)
#draw_Square(30,90,20,18)
