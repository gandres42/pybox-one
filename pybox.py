import pygame
import threading

values = {
    'l_joy_x': 0,
    'l_joy_y': 0,
    'r_joy_x': 0,
    'r_joy_y': 0,
    'd_pad_x': 0,
    'd_pad_y': 0,
    'lt': 0,
    'rt': 0,
    'lb': 0,
    'rb': 0,
    'select': 0,
    'start': 0,
    'r_joy_button': 0,
    'l_joy_button': 0,
    'a': 0,
    'b': 0,
    'x': 0,
    'y': 0
}

_listen_thread = None
_active = False
_controller = None

def listen():
    print("lets go!")
    print(_active)
    while _active:
        for event in pygame.event.get():
            # print(event.dict)
            if 'joy' in event.dict:
                if 'axis' in event.dict:
                    if event.dict['axis'] == 0:
                        values['l_joy_x'] = round(event.dict['value'], 3)
                    if event.dict['axis'] == 1:
                        values['l_joy_y'] = round(event.dict['value'] * -1, 3)
                    if event.dict['axis'] == 2:
                        values['lt'] = round((event.dict['value'] + 1) / 2, 3)
                    if event.dict['axis'] == 3:
                        values['r_joy_x'] = round(event.dict['value'], 3)
                    if event.dict['axis'] == 4:
                        values['r_joy_y'] = round(event.dict['value'] * -1, 3)
                    if event.dict['axis'] == 5:
                        values['rt'] = round((event.dict['value'] + 1) / 2, 3)

                if 'button' in event.dict:
                    if event.dict['button'] == 0:
                        if values['a'] == 0:
                            values['a'] = 1
                        else:
                            values['a'] = 0
                    if event.dict['button'] == 1:
                        if values['b'] == 0:
                            values['b'] = 1
                        else:
                            values['b'] = 0
                    if event.dict['button'] == 2:
                        if values['x'] == 0:
                            values['x'] = 1
                        else:
                            values['x'] = 0
                    if event.dict['button'] == 3:
                        if values['y'] == 0:
                            values['y'] = 1
                        else:
                            values['y'] = 0
                    if event.dict['button'] == 4:
                        if values['lb'] == 0:
                            values['lb'] = 1
                        else:
                            values['lb'] = 0
                    if event.dict['button'] == 5:
                        if values['rb'] == 0:
                            values['rb'] = 1
                        else:
                            values['rb'] = 0
                    if event.dict['button'] == 6:
                        if values['select'] == 0:
                            values['select'] = 1
                        else:
                            values['select'] = 0
                    if event.dict['button'] == 7:
                        if values['start'] == 0:
                            values['start'] = 1
                        else:
                            values['start'] = 0
                    if event.dict['button'] == 9:
                        if values['l_joy_button'] == 0:
                            values['l_joy_button'] = 1
                        else:
                            values['l_joy_button'] = 0
                    if event.dict['button'] == 10:
                        if values['r_joy_button'] == 0:
                            values['r_joy_button'] = 1
                        else:
                            values['r_joy_button'] = 0
                if 'hat' in event.dict:
                    values['d_pad_x'] = event.dict['value'][0]
                    values['d_pad_y'] = event.dict['value'][1]
                # print(values['rb'])
                print(values)

def init():
    global _listen_thread, _active, _controller
    pygame.init()
    pygame.joystick.init()
    _controller = pygame.joystick.Joystick(0)
    _controller.init()
    _listen_thread = threading.Thread(target=listen, daemon=True)
    _active = True
    _listen_thread.start()

def stop():
    global _listen_thread, _active
    _active = False
    if _listen_thread is not None:
        _listen_thread.join()
        _listen_thread = None