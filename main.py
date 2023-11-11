import pybox

def test():
    print(pybox.get_r_trigger())

pybox.init()
pybox.set_callback_r_trigger(test)
try:
    while True:
        pass
except KeyboardInterrupt:
    pybox.stop()