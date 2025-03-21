from inputs import get_gamepad
import RPi.GPIO as GPIO

keys = {
    "ABS_X": 127, #Left X Joystick
    "ABS_Y": 127, #Left Y Joystick
    "ABS_Z": 127, #Right X Joystick
    "ABS_RZ": 127, #Right Y Joystick
    "BTN_SELECT": 0, #Left Joystick Press
    "BTN_START": 0, #Right Joystick Press
    "BTN_TL": 0, #Left Trigger
    "BTN_TR": 0, #Right Trigger
    "BTN_WEST": 0, #Left Bump
    "BTN_Z": 0, #Right Bump
    "BTN_TL2": 0, #Button 9
    "BTN_TR2": 0, #Button 10
    "BTN_NORTH": 0, #Button 4
    "BTN_C": 0, #Button 3
    "BTN_EAST": 0, #Button 2
    "BTN_SOUTH": 0, #Button 1
    "ABS_HAT0X": 0, # -1 is Left D-Pad, 1 is Right D-Pad
    "ABS_HAT0Y": 0, # -1 is Up D-Pad, 1 is Down D-Pad

}

pins = {
    "right_motor_in1": 16, "right_motor_in2": 18, "right_motor_speed": 22,
    "left_motor_in1": 16, "left_motor_in2": 18, "left_motor_speed": 22,
}

try: 
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(pins["right_motor_in1"], GPIO.OUT, initial=GPIO.HIGH) #Right Motor In1 Setup
    GPIO.setup(pins["right_motor_in2"], GPIO.OUT, initial=GPIO.LOW) #Right Motor In2 Setup
    GPIO.setup(pins["right_motor_speed"], GPIO.OUT) #Right Motor PWM Setup
    #right_motor_pwm = GPIO.PWM(22, 0.87)
    #right_motor_pwm.start(50)

    while 1:
        '''
        #Non-Comprehension format
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            keys[event.code] = event.state
        '''
        [ keys.update({event.code: event.state}) for event in get_gamepad() ]
        
        '''
        equation = int( (keys["ABS_RZ"] / 127) * 50 )
        right_motor_pwm.ChangeDutyCycle( equation ) 
        print( equation )
        '''

except KeyboardInterrupt:
    #right_motor_pwm.stop()
    GPIO.cleanup()

