CONNECT_TYPE = 'rndis'  # rndis:有线连接,sta:组网连接,ap:路由直连

W_WIDTH = 640  # 窗口宽度
W_HEIGHT = 360  # 窗口高度

TITLE = 'ROBOMASTER'  # 窗口标题

CAMERA_SPEED = 200  # 摄像头基础移动速度
WHEEL_SPEED = 100  # 麦克纳姆轮基础移动速度

FONT_SIZE = 20  # 信息显示时的字体大小

WIFI = {
    'LEGO': '3.1415926',
    'LEPEN': '82202257',
    'APPLELEGO': '2.718281'
}


keyword_bind = {
    'info_blit': 'tab',  # 显示信息
    'reset_camera': 'r',  # 重置云台摄像头至车体中心位置
    'move_camera': ['up', 'down', 'left', 'right'],  # 移动摄像头
    'more_camera_speed': 'page up',  # 增加摄像头移动灵敏度
    'less_camera_speed': 'page down',  # 降低摄像头移动灵敏度

    'move_wheel': ['w', 's', 'a', 'd'],  # 麦克纳姆轮移动
}
keys = None  # 检测按钮按压
