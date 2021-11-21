# Authors: Mikhail Tinio
# Filename: QRCodeManeger.py
# Created: Nov 20, 2021
# Notes: Sources listed below

# "Generate and Read QR Code with Python" by AllTech
# https://www.youtube.com/watch?v=2QK942FPCw0

# "Scan QR codes and barcodes with Python" by Python enthusiast
# https://www.youtube.com/watch?v=IOhZqmSrjlE


import cv2 # use camera
import pyqrcode
from pyzbar.pyzbar import decode # decode qr codes

# One of pyzbar's dependancies
from PIL import Image


class QRCodeGenerator:
    
    def makeQR(string):
        qr = pyqrcode.create(string)
        qr.png('temp.png', scale=8)
        
        return qr
    
class QRCodeInterpreter:
    
    def readQR(string):
        
        # the "0" parameter is the index of the camera we want to use
        # change if you want a different camera
        camera = cv2.VideoCapture(0)
        
        # 3 - width
        camera.set(3, 640)
        # 4 - height
        camera.set(4, 480)
        
        # the camera is always on
        camera = True
        
        # while the camera is on
        while camera == True:
            
            # success is a boolean for whether or not the camera finds a QR
            # frame is a single image of the video stream
            success, frame = cap.read()
            
            for code in decode(frame):
                print(code.type)
                print(code.data.decode('utf-8'))
                
            # opens a camera window to see through the camera on the desktop
            cv2.imshow('QRBucks Interpreter', frame)
            
            # keeps the window open for 17 milliseconds
            # there are 17 ms in a 60 fps frame
            # change as needed
            cv2.waitKey(17)