# """CircuitPython Blink Example - the CircuitPython 'Hello, World!'"""
# import time
# import board
# import digitalio

# led = digitalio.DigitalInOut(board.GP17)
# led.direction = digitalio.Direction.OUTPUT

# """
# while True:
#     print("led on")
#     led.value = True
#     time.sleep(0.5)
    
#     print("led off") 
#     led.value = False 
#     time.sleep(0.5)
# """
# """
# """
# """

import time
import math
import board
import analogio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

LED_PIN = board.GP17
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

pin = digitalio.DigitalInOut(LED_PIN)
pin.direction = digitalio.Direction.OUTPUT

conversion_factor = 2 / 65535

class Joystick:
    def __init__(self, x_pin, y_pin, sw_pin, invert_x=False, invert_y=False):
        self.x_pin = analogio.AnalogIn(x_pin)
        self.invert_x = -1 if invert_x else 1
        self.y_pin = analogio.AnalogIn(y_pin)
        self.invert_y = -1 if invert_y else 1
        self.sw_pin = digitalio.DigitalInOut(sw_pin)
        self.sw_pin.switch_to_input(pull=digitalio.Pull.DOWN)
    
    def read_x(self):
        return (1 - self.x_pin.value * conversion_factor) * self.invert_x

    def read_y(self):
        return (1 - self.y_pin.value * conversion_factor) * self.invert_y

    def read_sw(self):
        return self.sw_pin.value

# Example usage:
left_joystick = Joystick(board.A0, board.A1, board.GP20, invert_x=True)
right_joystick = Joystick(board.A2, board.A3, board.GP21, invert_y=True)

text="Hello World"

output = ""
acceleration = 1
scalar = 5
last_cycle = time.monotonic()
while True:
    
	output = ""
	 
	left_joystick_x = left_joystick.read_x()
	left_joystick_y = left_joystick.read_y()
	right_joystick_x = right_joystick.read_x()
	right_joystick_y = right_joystick.read_y()
 
	output += f"LX:{left_joystick_x:>5.2f}  LY:{left_joystick_y:>5.2f}  LB:{left_joystick.read_sw():>1}"
	output += f" | RX:{right_joystick_x:>5.2f}  RY:{right_joystick_y:>5.2f}  RB:{right_joystick.read_sw():>1}"	
 
	# time in ms
	output += " " + str(round((time.monotonic() - last_cycle) * 1000)) + "ms"
	last_cycle = time.monotonic()
	print(output)
 
	# for i in range(0, 1000):
	# 	i ^ i
   
	deadzone = 0.05
	if abs(left_joystick_x) > deadzone or abs(left_joystick_y) > deadzone or abs(right_joystick_x) > deadzone or abs(right_joystick_y) > deadzone:
		#acceleration *= 1.005
		mouse.move(
			x=round(left_joystick_x + right_joystick_x * acceleration * scalar), 
			y=round(left_joystick_y + right_joystick_y * acceleration * scalar)
		)
	else:
		acceleration = 1
 
 
 
	#print("\c")
	if left_joystick.read_sw():
		keyboard_layout.write(text)
	#time.sleep(1)
# Adjust pin assignments as needed
# while True:
#     print("X:", joystick.read_x())
#     print("Y:", joystick.read_y())
#     print("SW:", joystick.read_sw())
# 	
#     time.sleep(0.1)