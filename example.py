import pybox

def sample_callback():
    print('callback says: \t', end="")
    print(pybox.get_r_trigger())

# call init to start listening for controller inputs
pybox.init()

# use set_callback commands to set a function to call when a button/joystick state changes
# callbacks take no paramaters, all state access must be done through get functiond
pybox.set_callback_r_trigger(sample_callback)

# this loop is wrapped in try except to catch KeyboardInterrupt and gracefully exit
try:
    while True:
        print('loop says: \t', end="")
        print(pybox.get_r_trigger())
except KeyboardInterrupt:
    # call stop to stop control loop, run before exit for a clean stop
    pybox.stop()