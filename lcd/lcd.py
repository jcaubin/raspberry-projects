import lcddriver
from time import *
import logging as log

log.basicConfig(level=log.INFO)

lcd = lcddriver.lcd()


lcd.lcd_display_string("antisteo on YT", 1)
#sleep(3)
lcd.lcd_display_string("LCD runtime is", 2)
lcd.lcd_display_string("picorder", 3)
lcd.lcd_display_string("connect me via I2C", 4)

for i in range(10,20):
    lcd.lcd_display_string(str(i), 3, 0)
    sleep (0.1)

lcd.lcd_clear()
lcd.lcd_display_string("end", 4)
sleep(1)
lcd.lcd_clear()

