import board
import busio
import digitalio

print("initializing i2c")

# Initialize I2C
i2c = busio.I2C(board.GP5, board.GP4)

# Set up interrupt on GP22
interrupt_pin = digitalio.DigitalInOut(board.GP22)
interrupt_pin.direction = digitalio.Direction.INPUT
interrupt_pin.pull = digitalio.Pull.UP

while not i2c.try_lock():
	pass

try:
	print("I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])
finally:
	i2c.unlock()

# Now you can check the value of interrupt_pin.value to see if an interrupt has occurred

while True:
	if not interrupt_pin.value:
		print("Interrupt occurred!")