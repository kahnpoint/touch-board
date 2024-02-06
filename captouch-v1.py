import time
import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

# I2C address of the device
DEVICE_ADDRESS = 0x31

# Register addresses (example)
COMMAND_SET_MODE = 0x00  # replace with actual register address
FIRMWARE_REVISION_REG = 0x01  # replace with actual register address
T841_ADCSRA = 0x02  # replace with actual register address
T841_DIDR0 = 0x03  # replace with actual register address
T841_PRR = 0x04  # replace with actual register address
COMMAND_CLOCK_PRESCALER = 0x05  # replace with actual register address
COMMAND_CAP_TOUCH = 0x06  # replace with actual register address
RETURN_VAL_REG_0 = 0x07  # replace with actual register address
RETURN_VAL_REG_1 = 0x08  # replace with actual register address
# Add the constants to your Python code
MODE_REGISTER_DEC = 0xAB
MODE_COMMAND = 0xAC
EXPECTED_CAPTOUCHWIRELING_FIRMWARE = 0x01  # replace with actual expected firmware version
T841_ADEN = 0x80  # replace with actual value
T841_PRSPI = 0x02  # replace with actual value
T841_PRUSART0 = 0x01  # replace with actual value
T841_PRUSART1 = 0x01  # replace with actual value
T841_CLOCK_PRESCALER_1 = 0x00  # replace with actual value
numSensors = 1  # replace with actual number of sensors

def _BV(bit):
	return 1 << bit


class CapTouchWireling:
	def __init__(self, sda, scl, addr = 0):
		self.address = DEVICE_ADDRESS + addr
		self.device = I2CDevice(busio.I2C(sda,scl), self.address)
		self.capTouchPins = [0]*numSensors

	# def write_byte(self, *args):
	# 	with self.device:
	# 		self.device.write(bytes(args))
        
	# def read(self, register_address):
	# 	with self.device:
	# 		self.device.write(bytes([register_address]))
	# 		result = bytearray(1)
	# 		self.device.readinto(result)
	# 	return result[0]

	# def begin(self):
	# 	self.write_byte(COMMAND_SET_MODE, MODE_REGISTER_DEC)
	# 	if self.read(FIRMWARE_REVISION_REG) != EXPECTED_CAPTOUCHWIRELING_FIRMWARE:
	# 		return 1

	# 	self.write_byte(T841_ADCSRA, _BV(T841_ADEN) | 4 | 1)
	# 	self.write_byte(T841_DIDR0, 0xAF)
	# 	self.write_byte(T841_PRR, _BV(T841_PRSPI) | _BV(T841_PRUSART0) | _BV(T841_PRUSART1))

	# 	self.write_byte(COMMAND_SET_MODE, MODE_COMMAND)
	# 	self.write_byte(COMMAND_CLOCK_PRESCALER, T841_CLOCK_PRESCALER_1)

	# 	for pin in range(numSensors):
	# 		self.capTouchCal[pin] = self.capTouchRead(pin)
	# 		self.overCalCount[pin] = 0

	# 	return 0

	# def capTouchRead(self, pin):
	# 	self.write_byte(COMMAND_CAP_TOUCH, self.capTouchPins[pin], 5)
	# 	time.sleep(0.001)
	# 	self.write_byte(COMMAND_SET_MODE, MODE_REGISTER_DEC)
	# 	value = self.read(RETURN_VAL_REG_0)
	# 	value += self.read(RETURN_VAL_REG_1) << 8
	# 	self.write_byte(COMMAND_SET_MODE, MODE_COMMAND)
	# 	return value
	
# Use the class
sda = board.GP5  # replace with actual SDA pin
scl = board.GP4  # replace with actual SCL pin
capTouchWireling = CapTouchWireling(sda, scl)
#capTouchWireling.begin()

# while True:
# 	for pin in range(numSensors):
# 		print("Pin", pin, ":", capTouchWireling.capTouchRead(pin))
# 	time.sleep(0.5)