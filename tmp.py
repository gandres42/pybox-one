_callbacks = {
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


for key in _callbacks.keys():
    print('def set_callback_' + key + "(func):")
    print('\t_callbacks[\'' + key + '\'] = func\n')