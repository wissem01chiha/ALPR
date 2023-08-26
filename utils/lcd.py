"""  

import  RPi.GPIO as GPIO
from    RPLCD import CharLCD

def lcd_display(message):
    GPIO.setwarnings(False)
    ## Set the GPIO numbering mode to BCM
    GPIO.setmode(GPIO.BOARD)
    lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],numbering_mode=GPIO.BOARD)
    lcd.clear()
    lcd.write_string(message)
    # Clean up GPIO before exiting
    # Clean up GPIO pins 

 """
   