# Authors: Mikhail Tinio
# Filename: QRCodeManeger.py
# Created: Nov 20, 2021
# Notes: Sources listed below

# "Generate and Read QR Code with Python"
# by AllTech
# https://www.youtube.com/watch?v=2QK942FPCw0

# "Scan QR codes and barcodes with Python"
# by Python enthusiast
# https://www.youtube.com/watch?v=IOhZqmSrjlE

# "QR Code In 10 lines of Python Code | Generate and Access QR Code Easily Using Python"
# by codebasics
# https://youtu.be/-GmJLI122ZM


import cv2
import pyqrcode


# One of pyzbar's dependancies
from PIL import Image


class QRCodeGenerator:
    
    def makeQR(self, filename, string):
        if '.png' in filename:
            pass
        else:
            filename = filename + '.png'
        qr = pyqrcode.create(string)
        qr.png(filename, scale=8)
        
        return qr
    
class QRCodeInterpreter:
    
    def readQRFromFile(filename):
        detector = cv2.QRCodeDetector()
        val, points, straight_qrcode = detector.detectAndDecode(cv2.imread(filename))
        print(val)
        return val
