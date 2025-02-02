from inputs import get_gamepad, DeviceManager

class Gamepad:
    def __init__(self):
        self.keys = {
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
    
    def update(self):
        '''
        #Non-Comprehension format
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            keys[event.code] = event.state
        '''
        [ self.keys.update({event.code: event.state}) for event in get_gamepad() ]

        '''
        equation = int( (keys["ABS_RZ"] / 127) * 50 )
        right_motor_pwm.ChangeDutyCycle( equation ) 
        print( equation )
        '''
