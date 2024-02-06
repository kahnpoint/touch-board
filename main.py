import busio
import time
import board
from attinydefs import *
from rainbowio import colorwheel
import neopixel
 
# redeclare _BV
def _BV(bit):
	return 1 << bit
 
# Create I2C bus
i2c = busio.I2C(board.GP1, board.GP0)
i2c.deinit()
i2c = busio.I2C(board.GP1, board.GP0, frequency=100_000)

# I2C address of the device
DEVICE_ADDRESS = 0x31

# Firmware revision register
FIRMWARE_REVISION_REG = 0x19
EXPECTED_CAPTOUCHWIRELING_FIRMWARE = 0x1A

# Mode register
MODE_REGISTER_INC = 0xAA
MODE_REGISTER_DEC = 0xAB
MODE_COMMAND = 0xAC
COMMAND_SET_MODE = 0x00
COMMAND_CAP_TOUCH = 0x13
COMMAND_CLOCK_PRESCALER = 0x0C

# Return value registers
RETURN_VAL_REG_0 = 0x1A
RETURN_VAL_REG_1 = 0x1B
RETURN_VAL_REG_2 = 0x1C
RETURN_VAL_REG_3 = 0x1D  

# print connected devices
while not i2c.try_lock():
	pass
devices = i2c.scan()
print("I2C addresses found:", [hex(device_address) for device_address in devices]) 

# set the register to decrement mode
i2c.writeto(DEVICE_ADDRESS, bytearray([COMMAND_SET_MODE, MODE_REGISTER_DEC]))
#time.sleep(0.001)  # Sleep for 1 millisecond
#output = bytearray(1)
#i2c.readfrom_into(DEVICE_ADDRESS, output)
#print("Output: ", output)  

i2c.unlock()
   
try:
	while not i2c.try_lock():
		pass
	buffer = bytearray(1) 
	#Read firmware revision register
	i2c.writeto(DEVICE_ADDRESS, bytearray([FIRMWARE_REVISION_REG]))
	#time.sleep(0.00001)  # Sleep for 1 millisecond
	i2c.readfrom_into(DEVICE_ADDRESS, buffer)
	print("Firmware Revision:", hex(buffer[0]))

	# Write to the device
	i2c.writeto(DEVICE_ADDRESS, bytearray([T841_ADCSRA, (_BV(T841_ADEN) | 4 | 1)]))
	i2c.writeto(DEVICE_ADDRESS, bytearray([T841_DIDR0, 0xAF]))
	i2c.writeto(DEVICE_ADDRESS, bytearray([T841_PRR, _BV(T841_PRSPI) | _BV(T841_PRUSART0) | _BV(T841_PRUSART1)]))
	i2c.writeto(DEVICE_ADDRESS, bytearray([COMMAND_SET_MODE, MODE_COMMAND]))
	i2c.writeto(DEVICE_ADDRESS, bytearray([COMMAND_CLOCK_PRESCALER, T841_CLOCK_PRESCALER_1]))
    
 
except Exception as e:
	print("Error:", e)
finally:
#	 i2c.deinit()  # Release the I2C bus 
	i2c.unlock()  
 
capTouchPins = [0, 1, 2, 3, 5, 7]

def readCapTouch(pin):
	value = 0
	while not i2c.try_lock(): 
		pass
	
	# Write to the device
	i2c.writeto(DEVICE_ADDRESS, bytes([COMMAND_CAP_TOUCH, capTouchPins[pin], 5]))
	#time.sleep(0.001)  # Sleep for 1 millisecond
	
	# Set the mode
	i2c.writeto(DEVICE_ADDRESS, bytes([COMMAND_SET_MODE, MODE_REGISTER_DEC]))   
	
	# Read two values
	buffer1 = bytearray(1)
	buffer2 = bytearray(1)
	i2c.writeto(DEVICE_ADDRESS, bytearray([RETURN_VAL_REG_0]))
	i2c.readfrom_into(DEVICE_ADDRESS, buffer1)
	i2c.writeto(DEVICE_ADDRESS, bytearray([RETURN_VAL_REG_1]))
	i2c.readfrom_into(DEVICE_ADDRESS, buffer2)
	  
	# Print the values of buffer1 and buffer2
	#print("buffer1: ", buffer1[0])
	#print("buffer2: ", buffer2[0])  
	
	# Combine the two values
	value = buffer1[0] + (buffer2[0] << 8)
	
	# Print the value
	#print("value: ", value)
	
	# Set the mode back
	i2c.writeto(DEVICE_ADDRESS, bytes([COMMAND_SET_MODE, MODE_COMMAND]))

	i2c.unlock()
	return value

pixel_pin = board.GP7
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=.1, auto_write=False)

now = time.monotonic()
cycles = 0

def update_light(pin):
	sensor_value = readCapTouch(pin)
	
	# account for the field produced by the circuitry on the back of the board
	if pin == 5:
		sensor_value -= 550
	else:
		sensor_value -= 450

	rounded_value = int(sensor_value / 100)
	output.append(rounded_value)

	is_sensor_touched = int(rounded_value > 0)

	if is_sensor_touched: 
		pixels[num_pixels-1-pin] = (rounded_value * 50, 250 - (rounded_value * 50), 0)
	else:
		pixels[num_pixels-1-pin] = (0, 0, 0)


while True:
	#print("Cap Touch: ")
	output = []
	list(map(lambda i: update_light(i), range(6)))
	# for i in range(6):
	# 	update_light(i)
 	
	pixels.show()
	cycles += 1
	if cycles == 10:
		print(int((time.monotonic() - now)/10*1000), "ms/cycle")
		now = time.monotonic()
		cycles = 0