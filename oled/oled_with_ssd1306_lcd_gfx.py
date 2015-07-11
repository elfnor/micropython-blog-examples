# hello world on SSD1306
# uses version of SSD1306.py and font.py
# https://github.com/jeffmer/micropython-upybbot/blob/master/ssd1306.py
# graphics library lcd_gfx.py from 
# http://forum.micropython.org/viewtopic.php?f=5&t=195&p=873&hilit=lcd_gfx#p873

import pyb
from ssd1306  import SSD1306
import lcd_gfx

oled = SSD1306(pinout={'dc': 'X4',
                       'res': 'X3'},
               height=64,
               external_vcc=False)
              

oled.poweron()
oled.init_display()

oled.clear()  
## text
oled.text('Hello World!', 20, 55)
oled.display()
pyb.delay(2000)

## draw straight lines
for x in [0, 127]:
    for y in range(64):
        oled.pixel(x, y, True)
for y in [0, 47, 48, 63]:
    for x in range(127): 
        oled.pixel(x, y, True)
    
oled.display()
pyb.delay(2000)             

## whole buffer        
b = [1] * 1024
for i in range(0, 1024, 16):   
    b[i] = 255
for i in range(0, 16):
    b[i] = 255
    
oled.buffer = bytearray(b)
oled.display()

pyb.delay(2000)  
oled.clear() 

## graphics example
lcd_gfx.drawCircle(35, 50, 10, oled, 1)
lcd_gfx.drawFillCircle(91, 50, 10, oled, 1)
lcd_gfx.drawLine(40, 20, 63, 5, oled, 1) 
lcd_gfx.drawLine(63, 5, 85, 5, oled, 1) 
lcd_gfx.drawFillTrie(63, 50, 63, 20, 50, 20, oled, 1)
lcd_gfx.drawTrie(63, 50, 63, 20, 78, 20, oled, 1)
lcd_gfx.drawRect(0, 0, 5, 5, oled, 1)
lcd_gfx.drawFillRect(122, 58, 5, 5, oled, 1)
oled.display()
