import sys
import time


from telemetrix import telemetrix

class ControlSystem:
    def __init__(self):
        self.board = telemetrix.Telemetrix()
    
    def setup(self):
        self.drive_left, self.drive_right = Motor12x5ALite(2,3), Motor12x5ALite(50,51)
        self.gripper, self.arm = MotorL298N(47,48,49), MotorL298N(44,45,46)

class MotorL298N(ControlSystem):
    def __init__(self,en_pinA, en_pinB,pwm_pin):
        self.en_pinA, self.en_pinB, self.pwm_pin = en_pinA, en_pinB,pwm_pin
        self.board.set_pin_mode_analog_output(pwm_pin)
        self.board.set_pin_mode_digital_output(en_pinA)
        self.board.set_pin_mode_digital_output(en_pinB)

    def power(self, motor_power):
        self.board.analog_write(abs(motor_power))
        if motor_power > 0:
            self.board.digital_write(self.en_pinA,0)
            self.board.digital_write(self.en_pinB,1)
        else:
            self.board.digital_write(self.en_pinA,1)
            self.board.digital_write(self.en_pinB,0)

class Motor12x5ALite(ControlSystem):
    def __init__(self,en_pin, pwm_pin):
        super().__init__()
        self.board.set_pin_mode_analog_output(pwm_pin)
        self.board.set_pin_mode_digital_output(en_pin)
    
    def power(self, motor_power):
        self.board.analog_write(abs(motor_power))
        if motor_power > 0:
            self.board.digital_write(self.en_pin,0)
        else:
            self.board.digital_write(self.en_pin,1)

robot = ControlSystem()
robot.setup()
# keep application running
while True:
    try:
        robot.drive_left.power(100)
        time.sleep(1)
        robot.drive_left.power(0)
        time.sleep(1)
        robot.drive_left.power(-100)
        time.sleep(1)
        robot.drive_left.power(0)
        time.sleep(1)
    except KeyboardInterrupt:
        robot.board.shutdown()
        sys.exit(0)