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
    'a_button': 0,
    'b_button': 0,
    'x_button': 0,
    'y_button': 0
}

_listen_thread = None
_active = False
_controller = None

def listen():
    print("lets go!")
    print(_active)
    while _active:
        for event in pygame.event.get():
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
                        if values['a_button'] == 0:
                            values['a_button'] = 1
                        else:
                            values['a_button'] = 0
                    if event.dict['button'] == 1:
                        if values['b_button'] == 0:
                            values['b_button'] = 1
                        else:
                            values['b_button'] = 0
                    if event.dict['button'] == 2:
                        if values['x_button'] == 0:
                            values['x_button'] = 1
                        else:
                            values['x_button'] = 0
                    if event.dict['button'] == 3:
                        if values['y_button'] == 0:
                            values['y_button'] = 1
                        else:
                            values['y_button'] = 0
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
        return values['l_joy_x']

def get_l_joy_y():
        return values['l_joy_y']

def get_r_joy_x():
        return values['r_joy_x']

def get_r_joy_y():
        return values['r_joy_y']

def get_d_pad_x():
        return values['d_pad_x']

def get_d_pad_y():
        return values['d_pad_y']

def get_lt():
        return values['lt']

def get_rt():
        return values['rt']

def get_lb():
        return values['lb']

def get_rb():
        return values['rb']

def get_select():
        return values['select']

def get_start():
        return values['start']

def get_r_joy_button():
        return values['r_joy_button']

def get_l_joy_button():
        return values['l_joy_button']

def get_a_button():
        return values['a_button']

def get_b_button():
        return values['b_button']

def get_x_button():
        return values['x_button']

def get_y_button():
        return values['y_button']