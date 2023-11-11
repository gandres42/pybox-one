import pybox

pybox.init()
try:
    while True:
        print(pybox.get_r_joy_x())
except KeyboardInterrupt:
    pybox.stop()