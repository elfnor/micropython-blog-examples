"""
Stepper motor control example using a A4988 carrier board 
and the nemastepper.py library available at 
https://github.com/jeffmer/micropython-upybbot
"""
import pyb

def disco(ms):
    """
    cycles LEDs on pyboard for ms milliseconds
    """
    leds = [pyb.LED(i) for i in range(1,5)]
    for l in leds:
        l.off()
    now = pyb.millis()
    n = 0
    try:
       while pyb.millis() <= now + ms:
          n = (n + 1) % 4
          leds[n].toggle()
          pyb.delay(50)
    finally:
        for l in leds:
            l.off()

from nemastepper import Stepper
motor1 = Stepper('Y1','Y2','Y3')

from pyb import Timer

def step_cb(t):
    motor1.do_step()
    
tim = Timer(8,freq=10000)
tim.callback(step_cb) #start interrupt routine

motor1.MAX_ACCEL = 1000
motor1.set_speed(1000)
disco(1000)  
motor1.set_speed(0)
motor1.set_speed(-1000)
disco(1000) 

motor1.set_speed(0)
motor1.set_off()

tim.deinit()
