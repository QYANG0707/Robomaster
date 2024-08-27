'''
通过 组网 连接robomaster
'''

import time
from robomaster import conn
from MyQR import myqr
from PIL import Image
from config import WIFI


QRCODE_NAME = "qrcode.png"

if __name__ == '__main__':

    helper = conn.ConnectionHelper()

    ssid = 'APPLELEGO'
    info = helper.build_qrcode_string(ssid=ssid, password=WIFI[ssid])

    myqr.run(words=info)
    time.sleep(1)
    img = Image.open(QRCODE_NAME)
    img.show()
    if helper.wait_for_connection():
        print("Connected!")
    else:
        print("Connect failed!")
