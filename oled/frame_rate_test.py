"""
Simple test of a 128 x 64 pixel OLED display with an ssd1306 driver chip on a SPI bus

|OLED |PYB |
|VCC  |3V3 |
|GND |GND|
|NC |-- |
|DIN |X8 MOSI |
|CLK |X6 SCK |
|CS |X5 SS |
|D/C |X4 |
|RES |X3 |
"""

import pyb
             
# from adafruit arduino
init_cmds = [0xAE, 0xD5, 0x80, 0xA8, 0x3F, 0xD3, 0x0, 0x40, 0x8D, 0x14, 0x20, 0x00, 0xA1, 0xC8,
             0xDA, 0x12, 0x81, 0xCF, 0xd9, 0xF1, 0xDB, 0x40, 0xA4, 0xA6, 0xAF]
              
display_cmds = [0x21, 0, 127, 0x22, 0, 7]
              
## set up SPI bus              
rate = 8000000

spi = pyb.SPI(1, pyb.SPI.MASTER, baudrate=rate, polarity=0, phase=0)  # SCK: Y6: MOSI: Y8
dc  = pyb.Pin('X4',  pyb.Pin.OUT_PP, pyb.Pin.PULL_DOWN)
res = pyb.Pin('X3', pyb.Pin.OUT_PP, pyb.Pin.PULL_DOWN)

def write_command(cmd):
    """
    write single command byte to ssd1306
    """
    dc.low()
    spi.send(cmd)    

## power on
res.high()
pyb.delay(1)
res.low()
pyb.delay(10)
res.high()

## init display
for cmd in init_cmds:
    write_command(cmd)

## clear display
buffer = bytearray(1024)
for cmd in display_cmds:
    write_command(cmd)
dc.high()
spi.send(buffer)

## line grid
b0 = [1] * 1024  # 8 horizontal lines

# set every  16th byte to 255
# should give 8 vertical lines
b1 = [0] * 1024
for i in range(0, 1024, 16):   
    b1[i] = 255

n = 1000
t0 = pyb.millis()
for i in range(n):
    buffer = bytearray(b0)
    for cmd in display_cmds:
        write_command(cmd)
    dc.high()
    spi.send(buffer) 
    
    buffer = bytearray(b1)
    for cmd in display_cmds:
      write_command(cmd)
    dc.high()
    spi.send(buffer) 

t1 = pyb.millis()

framespersecond = 1000* (n*2)/(t1-t0)
print(t1, t0, t1 - t0, framespersecond )
