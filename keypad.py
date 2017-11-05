from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
import requests


try:
	# Setup Keypad
	KEYPAD = [
	        ["1","2","3","A"],
	        ["4","5","6","B"],
	        ["7","8","9","C"],
	        ["*","0","#","D"]
	]
	
	COL_PINS = [12,6,13,16] # BCM numbering
	ROW_PINS = [19,26,20,21] # BCM numbering
	
	
	factory = rpi_gpio.KeypadFactory()
	
	keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
	
	count = 0
	numbersStr = ""
	
	def printKey(key):
	    global numbersStr, count
	    numbersStr += str(key)
	    print(numbersStr)
	    count = count +1
	    if count==4 :
	        r = requests.post('http://127.0.0.1:1880/pin', '{ "pinCode":"'+str(numbersStr)+'" }');
                count = 0
                numbersStr= ""
	    
	
	keypad.registerKeyPressHandler(printKey)
	
	print("Press buttons on your keypad. Ctrl+C to exit.")
	
	while True:
	       time.sleep(1)

except KeyboardInterrupt:
    print("Goodbye")
finally:
    keypad.cleanup()