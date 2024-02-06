from t841defs import *

def _BV(bit):
	return 1 << bit

COMMAND_SET_MODE = 0x00  # write mode- command, register access
COMMAND_SERVO_1 = 0x01 # write 16 bit pwm value 1
COMMAND_SERVO_2 = 0x02 # write 16 bit pwm value 2
COMMAND_SERVO_3 = 0x03 # write 16 bit pwm value 3
COMMAND_SERVO_4 = 0x04 # write 16 bit pwm value 4
COMMAND_MOTOR_1 = 0x05 # write first two 16 bit pwm values
COMMAND_MOTOR_2 = 0x06 # write second two 16 bit pwm values
COMMAND_ALL_PWM = 0x07 # write four 16 bit pwm values
COMMAND_TIMER_1 = 0x08 # write 16 bit timer 1 top value
COMMAND_TIMER_2 = 0x09 # write 16 bit timer 2 top value
COMMAND_PRESCALER_1 = 0x0A # write timer 1 prescaler
COMMAND_PRESCALER_2 = 0x0B # write timer 2 prescaler
COMMAND_CLOCK_PRESCALER = 0x0C # write system clock prescaler
COMMAND_SET_SLEEP_MODE = 0x0D # set sleep mode
COMMAND_SLEEP = 0x0E # go to sleep after I2C communication is done
COMMAND_SET_FAILSAFE_VALUES = 0x0F # set failsafe PWM values - default is 0
COMMAND_SET_FAILSAFE_PRESCALER = 0x10 # set failsafe timeout
COMMAND_SET_FAILSAFE_TIMEOUT = 0x11 # set failsafe timeout
COMMAND_ALL_PWM_8 = 0x12 # write four 8 bit pwm values
COMMAND_CAP_TOUCH = 0x13 # read cap touch value on pin

T841_CLOCK_PRESCALER_1 = 0x00
T841_CLOCK_PRESCALER_2 = 0x01
T841_CLOCK_PRESCALER_4 = 0x02
T841_CLOCK_PRESCALER_8 = 0x03
T841_CLOCK_PRESCALER_16 = 0x04
T841_CLOCK_PRESCALER_32 = 0x05
T841_CLOCK_PRESCALER_64 = 0x06
T841_CLOCK_PRESCALER_128 = 0x07
T841_CLOCK_PRESCALER_256 = 0x08

T841_TIMER_PRESCALER_0 = 0x00
T841_TIMER_PRESCALER_1 = 0x01
T841_TIMER_PRESCALER_8 = 0x02
T841_TIMER_PRESCALER_64 = 0x03
T841_TIMER_PRESCALER_256 = 0x04
T841_TIMER_PRESCALER_1024 = 0x05

T841_SLEEP_MODE_IDLE = 0
T841_SLEEP_MODE_ADC = _BV(T841_SM0)
T841_SLEEP_MODE_PWR_DOWN = _BV(T841_SM1)

MODE_REGISTER_INC = 0xAA
MODE_REGISTER_DEC = 0xAB
MODE_COMMAND = 0xAC

RETURN_VAL_REG_0 = 0x1A
RETURN_VAL_REG_1 = 0x1B
RETURN_VAL_REG_2 = 0x1C
RETURN_VAL_REG_3 = 0x1D

FIRMWARE_REVISION_REG = 0x19

NO_R_REMOVED =        0
R1_REMOVED =          1
R2_REMOVED =          2
R1_R2_REMOVED =       3
R3_REMOVED =          4
R1_R3_REMOVED =       5
R2_R3_REMOVED =       6
R1_R2_R3_REMOVED =    7
R4_REMOVED =          8
R1_R4_REMOVED =       9
R2_R4_REMOVED =       10
R1_R2_R4_REMOVED =    11
R3_R4_REMOVED =       12
R1_R3_R4_REMOVED =    13
R2_R3_R4_REMOVED =    14
R1_R2_R3_R4_REMOVED = 15
