import pygame
import threading

_values = {
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
    'a_button': 0,
    'b_button': 0,
    'x_button': 0,
    'y_button': 0
}

_callbacks = {
    'l_joy_x': None,
    'l_joy_y': None,
    'r_joy_x': None,
    'r_joy_y': None,
    'd_pad_x': None,
    'd_pad_y': None,
    'lt': None,
    'rt': None,
    'lb': None,
    'rb': None,
    'select': None,
    'start': None,
    'r_joy_button': None,
    'l_joy_button': None,
    'a_button': None,
    'b_button': None,
    'x_button': None,
    'y_button': None
}


_listen_thread = None
_active = False
_controller = None

def listen():
    while _active:
        for event in pygame.event.get():
            if 'joy' in event.dict:
                if 'axis' in event.dict:
                    if event.dict['axis'] == 0:
                        _values['l_joy_x'] = round(event.dict['value'], 3)
                    if event.dict['axis'] == 1:
                        _values['l_joy_y'] = round(event.dict['value'] * -1, 3)
                    if event.dict['axis'] == 2:
                        _values['lt'] = round((event.dict['value'] + 1) / 2, 3)
                    if event.dict['axis'] == 3:
                        _values['r_joy_x'] = round(event.dict['value'], 3)
                    if event.dict['axis'] == 4:
                        _values['r_joy_y'] = round(event.dict['value'] * -1, 3)
                    if event.dict['axis'] == 5:
                        _values['rt'] = round((event.dict['value'] + 1) / 2, 3)

                if 'button' in event.dict:
                    if event.dict['button'] == 0:
                        if _values['a_button'] == 0:
                            _values['a_button'] = 1
                        else:
                            _values['a_button'] = 0
                    if event.dict['button'] == 1:
                        if _values['b_button'] == 0:
                            _values['b_button'] = 1
                        else:
                            _values['b_button'] = 0
                    if event.dict['button'] == 2:
                        if _values['x_button'] == 0:
                            _values['x_button'] = 1
                        else:
                            _values['x_button'] = 0
                    if event.dict['button'] == 3:
                        if _values['y_button'] == 0:
                            _values['y_button'] = 1
                        else:
                            _values['y_button'] = 0
                    if event.dict['button'] == 4:
                        if _values['lb'] == 0:
                            _values['lb'] = 1
                        else:
                            _values['lb'] = 0
                    if event.dict['button'] == 5:
                        if _values['rb'] == 0:
                            _values['rb'] = 1
                        else:
                            _values['rb'] = 0
                    if event.dict['button'] == 6:
                        if _values['select'] == 0:
                            _values['select'] = 1
                        else:
                            _values['select'] = 0
                    if event.dict['button'] == 7:
                        if _values['start'] == 0:
                            _values['start'] = 1
                        else:
                            _values['start'] = 0
                    if event.dict['button'] == 9:
                        if _values['l_joy_button'] == 0:
                            _values['l_joy_button'] = 1
                        else:
                            _values['l_joy_button'] = 0
                    if event.dict['button'] == 10:
                        if _values['r_joy_button'] == 0:
                            _values['r_joy_button'] = 1
                        else:
                            _values['r_joy_button'] = 0
                if 'hat' in event.dict:
                    _values['d_pad_x'] = event.dict['value'][0]
                    _values['d_pad_y'] = event.dict['value'][1]
                # print(values['rb'])
                # print(values)

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

def get_l_joy_x():
        return _values['l_joy_x']

def get_l_joy_y():
        return _values['l_joy_y']

def get_r_joy_x():
        return _values['r_joy_x']

def get_r_joy_y():
        return _values['r_joy_y']

def get_d_pad_x():
        return _values['d_pad_x']

def get_d_pad_y():
        return _values['d_pad_y']

def get_lt():
        return _values['lt']

def get_rt():
        return _values['rt']

def get_lb():
        return _values['lb']

def get_rb():
        return _values['rb']

def get_select():
        return _values['select']

def get_start():
        return _values['start']

def get_r_joy_button():
        return _values['r_joy_button']

def get_l_joy_button():
        return _values['l_joy_button']

def get_a_button():
        return _values['a_button']

def get_b_button():
        return _values['b_button']

def get_x_button():
        return _values['x_button']

def get_y_button():
        return _values['y_button']