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

for key in values.keys():
    print('def get_' + key + "():")
    print('\treturn values[\'' + key + '\']\n')
    # print(key)