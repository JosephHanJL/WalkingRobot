from math import sin, cos, pi
from lx16a import *
import time

LX16A.initialize("COM3")
range1 = 25
range2 = 35
range3 = 8
range4 = 5
routine = 1
try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
    servo7.set_angle_limits(0, 240)
    servo8.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
t = 0

while True:
    if routine == 1:
        try:
            # servo1.move(sin(t+pi) * range1/2 + 65+range1/2)
            # servo2.move(sin(t+pi) * range2/2 + 16+range2/2)
            # servo3.move(sin(t) * range1/2 + 145+range1/2)
            # servo4.move(sin(t) * range2/2 + 110+range2/2)
            # servo5.move(sin(t+pi) * range1/2 + 85+range1/2)
            # servo6.move(sin(t+pi) * range2/2 + 105+range2/2)
            # servo7.move(sin(t) * range1/2 + 85+range1/2)
            # servo8.move(sin(t) * range2/2 + 75+range2/2)
            servo1.move(sin(t) * range2 + 86.16)
            servo2.move(-sin(t) * range1 + 140.40)
            servo5.move(-sin(t) * range2 + 129.84)
            servo6.move(sin(t) * range1 + 106.32)
            
            servo3.move(-sin(t-pi/2) * range2 + 80.40)
            servo4.move(sin(t-pi/2) * range1 + 137.04)
            servo7.move(sin(t-pi/2) * range2 + 175.68)
            servo8.move(-sin(t-pi/2) * range1 + 101.76)

            time.sleep(0.01)
            t += 0.1
        except ServoTimeoutError as e:
            print(f"Servo {e.id_} is not responding. Exiting...")
            quit()
    else:
        try:
            servo1.move(sin(t) * range4 + 62.64)
            servo2.move(-sin(t) * range3 + 176.88)
            servo5.move(-sin(t) * range4 + 140.4)
            servo6.move(sin(t) * range3 + 58.32)
            
            servo3.move(-sin(t+pi/2) * range4 + 66)
            servo4.move(sin(t+pi/2) * range3 + 180)
            servo7.move(sin(t+pi/2) * range4 + 174.96)
            servo8.move(-sin(t+pi/2) * range3 + 60)
            time.sleep(0.05)
            t += 0.1
        except ServoTimeoutError as e:
            print(f"Servo {e.id_} is not responding. Exiting...")
            quit()       