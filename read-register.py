    
# I2C address of the device
DEVICE_ADDRESS = 0x31

# Register address (example)
REGISTER_ADDRESS = 0x00  # replace with actual register address

# Initialize I2C bus
i2c = busio.I2C(board.GP5, board.GP4) 

# Create I2C device
device = I2CDevice(i2c, DEVICE_ADDRESS)

# Read a byte from the device
def read_register(register_address):
    with device:
        device.write(bytes([register_address]))
        result = bytearray(1)
        device.readinto(result)
    return result[0]

# Use the function
value = read_register(REGISTER_ADDRESS)
print(f"Read value {value} from register {REGISTER_ADDRESS}")


