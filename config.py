CONNECT_TYPE = 'rndis'  # rndis,sta,ap

W_WIDTH = 640
W_HEIGHT = 360

TITLE = 'ROBOMASTER'

CAMERA_SPEED = 200
WHEEL_SPEED = 100

WIFI = {
    'LEGO': '3.1415926',
    'LEPEN': '82202257',
    'APPLELEGO': '2.718281'
}
keyword_bind = {
    'info_blit': 'tab',
    'test_a': 'a',
    'test_b': 'b',
    'reset_camera': 'r',  # 重置云台摄像头至车体中心位置
    'move_camera': ['up', 'down', 'left', 'right'],
    'more_camera_speed': 'page up',
    'less_camera_speed': 'page down',

    'move_wheel': ['w', 's', 'a', 'd'],
}
keys = None
