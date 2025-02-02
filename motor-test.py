import sys
import time


from telemetrix import telemetrix

board = telemetrix.Telemetrix()
board.set_pin_mode_analog_output(3)
board.set_pin_mode_digital_output(2)
    
# keep application running
while True:
    try:
        board.analog_write(3,0)
        board.digital_write(2,0)
        time.sleep(1)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)