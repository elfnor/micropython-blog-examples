"""
Stepper motor control example using a A4988 carrier board 
"""
import pyb

dir_pin = pyb.Pin('Y1', pyb.Pin.OUT_PP)
step_pin = pyb.Pin('Y2', pyb.Pin.OUT_PP)
enable_pin =pyb.Pin('Y3', pyb.Pin.OUT_PP)

enable_pin.high()  # high is stop
dir_pin.high()     # high is CCW looking down on shaft

enable_pin.low()
for i in range(1000):
        step_pin.high()
        pyb.udelay(2)
        step_pin.low()
        pyb.udelay(1000)

dir_pin.low()

for i in range(1000):
        step_pin.high()
        pyb.udelay(2)
        step_pin.low()
        pyb.udelay(1000)

enable_pin.high()

#Brake motor draws full current
enable_pin.low()
pyb.delay(5000)
enable_pin.high()
