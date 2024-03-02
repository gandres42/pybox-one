import pybox

controller = pybox.UltimateC()

def sample_callback():
    print('callback says: \t', end="")
    print(controller.get_r_trigger())

# use set_callback commands to set a function to call when a button/joystick state changes
# callbacks take no paramaters, all state access must be done through get functiond
controller.set_callback_r_trigger(sample_callback)

# this loop is wrapped in try except to catch KeyboardInterrupt and gracefully exit
while True:
    # print('loop says: \t', end="")
    # print(controller.get_r_trigger())
    pass