import sys
import time
from telemetrix import telemetrix
from mygamepad import Gamepad

class ControlSystem:
    def __init__(self):
        self.gamepad = Gamepad()
        self.board = telemetrix.Telemetrix()
        self.drive_left, self.drive_right = Motor12x5ALite(3,2, self.board), Motor12x5ALite(5,4, self.board)
        self.gripper, self.arm = MotorL298N(47,48,49, self.board), MotorL298N(44,45,46, self.board)
    
    def drivetrain(self):
        self.drive_left.power(int( (self.gamepad.keys["ABS_Y"] - 128) * 2 ))
        self.drive_right.power(int( (self.gamepad.keys["ABS_RZ"] - 128) * -2 ))

class MotorL298N:
    def __init__(self,en_pinA, en_pinB,pwm_pin, board):
        self.board = board
        self.en_pinA, self.en_pinB, self.pwm_pin = en_pinA, en_pinB,pwm_pin
        self.board.set_pin_mode_analog_output(self.pwm_pin)
        self.board.set_pin_mode_digital_output(self.en_pinA)
        self.board.set_pin_mode_digital_output(self.en_pinB)

    def power(self, motor_power):
        self.board.analog_write(self.pwm_pin, abs(motor_power))
        if motor_power > 0:
            self.board.digital_write(self.en_pinA,0)
            self.board.digital_write(self.en_pinB,1)
        else:
            self.board.digital_write(self.en_pinA,1)
            self.board.digital_write(self.en_pinB,0)

class Motor12x5ALite():
    def __init__(self,en_pin, pwm_pin, board):
        self.board = board
        self.en_pin, self.pwm_pin = en_pin, pwm_pin
        self.board.set_pin_mode_analog_output(self.pwm_pin)
        self.board.set_pin_mode_digital_output(self.en_pin)
    
    def power(self, motor_power):
        self.board.analog_write(self.pwm_pin, abs(motor_power))
        if motor_power > 0:
            self.board.digital_write(self.en_pin,0)
        else:
            self.board.digital_write(self.en_pin,1)
    
    

robot = ControlSystem()
# keep application running
while True:
    try:
        robot.drivetrain()
        time.sleep(100)
    except KeyboardInterrupt:
        robot.board.shutdown()
        sys.exit(0)