import pybox

pybox.init()
try:
    while True:
        # print(pybox.get_r_joy_x())
        pass
except KeyboardInterrupt:
    pybox.stop()