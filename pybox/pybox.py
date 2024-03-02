import pygame
from multiprocessing import Process, Value, Lock, Event, Queue
from threading import Thread

class UltimateC:
    def __init__(self, controller_type = None) -> None:
        self.l_joy_x = Value('d', 0)
        self.l_joy_y = Value('d', 0)
        self.r_joy_x = Value('d', 0)
        self.r_joy_y = Value('d', 0)
        self.d_pad_x = Value('d', 0)
        self.d_pad_y = Value('d', 0)
        self.l_trigger = Value('d', 0)
        self.r_trigger = Value('d', 0)
        self.l_bumper = Value('d', 0)
        self.r_bumper = Value('d', 0)
        self.select = Value('d', 0)
        self.start = Value('d', 0)
        self.r_joy_button = Value('d', 0)
        self.l_joy_button = Value('d', 0)
        self.a_button = Value('d', 0)
        self.b_button = Value('d', 0)
        self.x_button = Value('d', 0)
        self.y_button = Value('d', 0)

        self._callbacks = {
            'l_joy_x': None,
            'l_joy_y': None,
            'r_joy_x': None,
            'r_joy_y': None,
            'd_pad_x': None,
            'd_pad_y': None,
            'l_trigger': None,
            'r_trigger': None,
            'l_bumper': None,
            'r_bumper': None,
            'select': None,
            'start': None,
            'r_joy_button': None,
            'l_joy_button': None,
            'a_button': None,
            'b_button': None,
            'x_button': None,
            'y_button': None
        }

        pygame.init()
        pygame.joystick.init()
        _controller = pygame.joystick.Joystick(0)
        _controller.init()

        self._stop_flag = Event()
        self._listen_process = Process(target=self._ultimate_c_listen)
        self._callback_thread = Thread(target=self._callback_listen, daemon=True)
        self._val_lock = Lock()
        self._callback_queue = Queue()
        self._callback_thread.start()
        self._listen_process.start()

    def __del__(self):
        self._stop_flag.set()

    def _call(self, key):
        self._callback_queue.put(key)
        

    def _callback_listen(self):
        while not self._stop_flag.is_set():
            func = self._callback_queue.get()
            if self._callbacks[func] is not None:
                self._callbacks[func]()

    def _ultimate_c_listen(self):
        while not self._stop_flag.is_set():
            for event in pygame.event.get():
                if 'joy' in event.dict:
                    if 'axis' in event.dict:
                        if event.dict['axis'] == 0:
                            self.l_joy_x.value = round(event.dict['value'], 3)
                            self._call('l_joy_x')
                        if event.dict['axis'] == 1:
                            self.l_joy_y.value = round(event.dict['value'] * -1, 3)
                            self._call('l_joy_y')
                        if event.dict['axis'] == 2:
                            self.r_joy_x.value = round(event.dict['value'], 3)
                            self._call('r_joy_x')
                        if event.dict['axis'] == 3:
                            self.r_joy_y.value = round(event.dict['value'] * -1, 3)
                            self._call('r_joy_y')
                        if event.dict['axis'] == 4:
                            self.r_trigger.value = round((event.dict['value'] + 1) / 2, 3)
                            self._call('r_trigger')
                        if event.dict['axis'] == 5:
                            self.l_trigger.value = round((event.dict['value'] + 1) / 2, 3)
                            self._call('l_trigger')
                    if 'button' in event.dict:
                        if event.dict['button'] == 0:
                            if self.a_button.value == 0:
                                self.a_button.value = 1
                            else:
                                self.a_button.value = 0
                            self._call('a_button')
                        if event.dict['button'] == 1:
                            if self.b_button.value == 0:
                                self.b_button.value = 1
                            else:
                                self.b_button.value = 0
                            self._call('a_button')
                        if event.dict['button'] == 2:
                            if self.x_button.value == 0:
                                self.x_button.value = 1
                            else:
                                self.x_button.value = 0
                            self._call('x_button')
                        if event.dict['button'] == 3:
                            if self.y_button.value == 0:
                                self.y_button.value = 1
                            else:
                                self.y_button.value = 0
                            self._call('y_button')
                        if event.dict['button'] == 4:
                            if self.l_bumper.value == 0:
                                self.l_bumper.value = 1
                            else:
                                self.l_bumper.value = 0
                            self._call('l_bumper')
                        if event.dict['button'] == 5:
                            if self.r_bumper.value == 0:
                                self.r_bumper.value = 1
                            else:
                                self.r_bumper.value = 0
                            self._call('r_bumper')
                        if event.dict['button'] == 6:
                            if self.select.value == 0:
                                self.select.value = 1
                            else:
                                self.select.value = 0
                            self._call('select')
                        if event.dict['button'] == 7:
                            if self.start.value == 0:
                                self.start.value = 1
                            else:
                                self.start.value = 0
                        if event.dict['button'] == 9:
                            if self.l_joy_button.value == 0:
                                self.l_joy_button.value = 1
                            else:
                                self.l_joy_button.value = 0
                            self._call('l_joy_button')
                        if event.dict['button'] == 10:
                            if self.r_joy_button.value == 0:
                                self.r_joy_button.value = 1
                            else:
                                self.r_joy_button.value = 0
                            self._call('r_joy_button')
                    if 'hat' in event.dict:
                        self.d_pad_x.value = event.dict['value'][0]
                        self.d_pad_y.value = event.dict['value'][1]

    def get_l_joy_x(self):
            return self.l_joy_x.value

    def get_l_joy_y(self):
            return self.l_joy_y.value

    def get_r_joy_x(self):
            return self.r_joy_x.value

    def get_r_joy_y(self):
            return self.r_joy_y.value

    def get_d_pad_x(self):
            return self.d_pad_x.value

    def get_d_pad_y(self):
            return self.d_pad_y.value

    def get_l_trigger(self):
            return self.l_trigger.value

    def get_r_trigger(self):
            return self.r_trigger.value

    def get_l_bumper(self):
            return self.l_bumper.value

    def get_r_bumper(self):
            return self.r_bumper.value

    def get_select(self):
            return self.select.value

    def get_start(self):
            return self.start.value

    def get_r_joy_button(self):
            return self.r_joy_button.value

    def get_l_joy_button(self):
            return self.l_joy_button.value

    def get_a_button(self):
            return self.a_button.value

    def get_b_button(self):
            return self.b_button.value

    def get_x_button(self):
            return self.x_button.value

    def get_y_button(self):
            return self.y_button.value

    def set_callback_l_joy_x(self, func):
            self._callbacks['l_joy_x'] = func

    def set_callback_l_joy_y(self, func):
            self._callbacks['l_joy_y'] = func

    def set_callback_r_joy_x(self, func):
            self._callbacks['r_joy_x'] = func

    def set_callback_r_joy_y(self, func):
            self._callbacks['r_joy_y'] = func

    def set_callback_d_pad_x(self, func):
            self._callbacks['d_pad_x'] = func

    def set_callback_d_pad_y(self, func):
            self._callbacks['d_pad_y'] = func

    def set_callback_l_trigger(self, func):
            self._callbacks['l_trigger'] = func

    def set_callback_r_trigger(self, func):
            self._callbacks['r_trigger'] = func

    def set_callback_l_bumper(self, func):
            self._callbacks['l_bumper'] = func

    def set_callback_r_bumper(self, func):
            self._callbacks['r_bumper'] = func

    def set_callback_select(self, func):
            self._callbacks['select'] = func

    def set_callback_start(self, func):
            self._callbacks['start'] = func

    def set_callback_r_joy_button(self, func):
            self._callbacks['r_joy_button'] = func

    def set_callback_l_joy_button(self, func):
            self._callbacks['l_joy_button'] = func

    def set_callback_a_button(self, func):
            self._callbacks['a_button'] = func

    def set_callback_b_button(self, func):
            self._callbacks['b_button'] = func

    def set_callback_x_button(self, func):
            self._callbacks['x_button'] = func

    def set_callback_y_button(self, func):
        self._callbacks['y_button'] = func

class XboxOne:
    def __init__(self, controller_type = None) -> None:
        self.l_joy_x = Value('d', 0)
        self.l_joy_y = Value('d', 0)
        self.r_joy_x = Value('d', 0)
        self.r_joy_y = Value('d', 0)
        self.d_pad_x = Value('d', 0)
        self.d_pad_y = Value('d', 0)
        self.l_trigger = Value('d', 0)
        self.r_trigger = Value('d', 0)
        self.l_bumper = Value('d', 0)
        self.r_bumper = Value('d', 0)
        self.select = Value('d', 0)
        self.start = Value('d', 0)
        self.r_joy_button = Value('d', 0)
        self.l_joy_button = Value('d', 0)
        self.a_button = Value('d', 0)
        self.b_button = Value('d', 0)
        self.x_button = Value('d', 0)
        self.y_button = Value('d', 0)

        self._callbacks = {
            'l_joy_x': None,
            'l_joy_y': None,
            'r_joy_x': None,
            'r_joy_y': None,
            'd_pad_x': None,
            'd_pad_y': None,
            'l_trigger': None,
            'r_trigger': None,
            'l_bumper': None,
            'r_bumper': None,
            'select': None,
            'start': None,
            'r_joy_button': None,
            'l_joy_button': None,
            'a_button': None,
            'b_button': None,
            'x_button': None,
            'y_button': None
        }

        pygame.init()
        pygame.joystick.init()
        _controller = pygame.joystick.Joystick(0)
        _controller.init()

        self._stop_flag = Event()
        self._listen_process = Process(target=self._xbox_listen)
        self._callback_thread = Thread(target=self._callback_listen, daemon=True)
        self._val_lock = Lock()
        self._callback_queue = Queue()
        self._callback_thread.start()
        self._listen_process.start()

    def __del__(self):
        self._stop_flag.set()

    def _call(self, key):
        self._callback_queue.put(key)
        

    def _callback_listen(self):
        while not self._stop_flag.is_set():
            func = self._callback_queue.get()
            if self._callbacks[func] is not None:
                self._callbacks[func]()

    def _xbox_listen(self):
        while not self._stop_flag.is_set():
            for event in pygame.event.get():
                if 'joy' in event.dict:
                    if 'axis' in event.dict:
                        if event.dict['axis'] == 0:
                            self.l_joy_x.value = round(event.dict['value'], 3)
                            self._call('l_joy_x')
                        if event.dict['axis'] == 1:
                            self.l_joy_y.value = round(event.dict['value'] * -1, 3)
                            self._call('l_joy_y')
                        if event.dict['axis'] == 2:
                            self.r_joy_x.value = round(event.dict['value'], 3)
                            self._call('r_joy_x')
                        if event.dict['axis'] == 3:
                            self.r_joy_y.value = round(event.dict['value'] * -1, 3)
                            self._call('r_joy_y')
                        if event.dict['axis'] == 4:
                            self.r_trigger.value = round((event.dict['value'] + 1) / 2, 3)
                            self._call('r_trigger')
                        if event.dict['axis'] == 5:
                            self.l_trigger.value = round((event.dict['value'] + 1) / 2, 3)
                            self._call('l_trigger')
                    if 'button' in event.dict:
                        if event.dict['button'] == 0:
                            if self.a_button.value == 0:
                                self.a_button.value = 1
                            else:
                                self.a_button.value = 0
                            self._call('a_button')
                        if event.dict['button'] == 1:
                            if self.b_button.value == 0:
                                self.b_button.value = 1
                            else:
                                self.b_button.value = 0
                            self._call('a_button')
                        if event.dict['button'] == 2:
                            if self.x_button.value == 0:
                                self.x_button.value = 1
                            else:
                                self.x_button.value = 0
                            self._call('x_button')
                        if event.dict['button'] == 3:
                            if self.y_button.value == 0:
                                self.y_button.value = 1
                            else:
                                self.y_button.value = 0
                            self._call('y_button')
                        if event.dict['button'] == 4:
                            if self.l_bumper.value == 0:
                                self.l_bumper.value = 1
                            else:
                                self.l_bumper.value = 0
                            self._call('l_bumper')
                        if event.dict['button'] == 5:
                            if self.r_bumper.value == 0:
                                self.r_bumper.value = 1
                            else:
                                self.r_bumper.value = 0
                            self._call('r_bumper')
                        if event.dict['button'] == 6:
                            if self.select.value == 0:
                                self.select.value = 1
                            else:
                                self.select.value = 0
                            self._call('select')
                        if event.dict['button'] == 7:
                            if self.start.value == 0:
                                self.start.value = 1
                            else:
                                self.start.value = 0
                        if event.dict['button'] == 9:
                            if self.l_joy_button.value == 0:
                                self.l_joy_button.value = 1
                            else:
                                self.l_joy_button.value = 0
                            self._call('l_joy_button')
                        if event.dict['button'] == 10:
                            if self.r_joy_button.value == 0:
                                self.r_joy_button.value = 1
                            else:
                                self.r_joy_button.value = 0
                            self._call('r_joy_button')
                    if 'hat' in event.dict:
                        self.d_pad_x.value = event.dict['value'][0]
                        self.d_pad_y.value = event.dict['value'][1]

    def get_l_joy_x(self):
            return self.l_joy_x.value

    def get_l_joy_y(self):
            return self.l_joy_y.value

    def get_r_joy_x(self):
            return self.r_joy_x.value

    def get_r_joy_y(self):
            return self.r_joy_y.value

    def get_d_pad_x(self):
            return self.d_pad_x.value

    def get_d_pad_y(self):
            return self.d_pad_y.value

    def get_l_trigger(self):
            return self.l_trigger.value

    def get_r_trigger(self):
            return self.r_trigger.value

    def get_l_bumper(self):
            return self.l_bumper.value

    def get_r_bumper(self):
            return self.r_bumper.value

    def get_select(self):
            return self.select.value

    def get_start(self):
            return self.start.value

    def get_r_joy_button(self):
            return self.r_joy_button.value

    def get_l_joy_button(self):
            return self.l_joy_button.value

    def get_a_button(self):
            return self.a_button.value

    def get_b_button(self):
            return self.b_button.value

    def get_x_button(self):
            return self.x_button.value

    def get_y_button(self):
            return self.y_button.value

    def set_callback_l_joy_x(self, func):
            self._callbacks['l_joy_x'] = func

    def set_callback_l_joy_y(self, func):
            self._callbacks['l_joy_y'] = func

    def set_callback_r_joy_x(self, func):
            self._callbacks['r_joy_x'] = func

    def set_callback_r_joy_y(self, func):
            self._callbacks['r_joy_y'] = func

    def set_callback_d_pad_x(self, func):
            self._callbacks['d_pad_x'] = func

    def set_callback_d_pad_y(self, func):
            self._callbacks['d_pad_y'] = func

    def set_callback_l_trigger(self, func):
            self._callbacks['l_trigger'] = func

    def set_callback_r_trigger(self, func):
            self._callbacks['r_trigger'] = func

    def set_callback_l_bumper(self, func):
            self._callbacks['l_bumper'] = func

    def set_callback_r_bumper(self, func):
            self._callbacks['r_bumper'] = func

    def set_callback_select(self, func):
            self._callbacks['select'] = func

    def set_callback_start(self, func):
            self._callbacks['start'] = func

    def set_callback_r_joy_button(self, func):
            self._callbacks['r_joy_button'] = func

    def set_callback_l_joy_button(self, func):
            self._callbacks['l_joy_button'] = func

    def set_callback_a_button(self, func):
            self._callbacks['a_button'] = func

    def set_callback_b_button(self, func):
            self._callbacks['b_button'] = func

    def set_callback_x_button(self, func):
            self._callbacks['x_button'] = func

    def set_callback_y_button(self, func):
        self._callbacks['y_button'] = func