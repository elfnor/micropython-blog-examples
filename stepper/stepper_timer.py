"""
Stepper motor control example using a A4988 carrier board 
and a Timer
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

def motor_cb1(t):
    step_pin.high()
    pyb.udelay(2)
    step_pin.low()

dir_pin = pyb.Pin('Y1', pyb.Pin.OUT_PP)
step_pin = pyb.Pin('Y2', pyb.Pin.OUT_PP)
enable_pin =pyb.Pin('Y3', pyb.Pin.OUT_PP)

enable_pin.high()  # high is stop
dir_pin.high()     # high is CCW looking down on shaft

tim1 = pyb.Timer(1, freq=1)

tim1.callback(motor_cb1)
tim1.init(freq = 1000)

enable_pin.low()
dir_pin.low()
disco(1000)
dir_pin.high()
disco(1000)
enable_pin.high()

tim1.deinit()
