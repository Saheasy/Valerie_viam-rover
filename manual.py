from inputs import get_gamepad
while 1:
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
        if event.code == 'BTN_C':
            print("Gotcha")