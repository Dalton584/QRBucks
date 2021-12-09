# Authors: Dalton Walker & Mikhail Tinio
# Filename: QRBucks Interpreter.py
# Created: Nov 20, 2021
# Notes: Sources listed below

# "How to Create and Manipulate SQL Databases with Python" by Craig Dickson
# https://www.freecodecamp.org/news/connect-python-with-sql/

# "Scan QR codes and barcodes with Python"
# by Python enthusiast
# https://www.youtube.com/watch?v=IOhZqmSrjlE

# "QR Code In 10 lines of Python Code | Generate and Access QR Code Easily Using Python"
# by codebasics
# https://youtu.be/-GmJLI122ZM


import mysql.connector
from mysql.connector import Error
import cv2
from pyzbar.pyzbar import decode

# One of pyzbar's dependancies
from PIL import Image


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def formatString(query):
    query = query.strip('(')
    query = query.strip(',)')
    return query

def readQRFromCamera():
        cap = cv2.VideoCapture(0)
        cap.set(3, 640) # 3 - Width
        cap.set(4, 480) # 4 - Height
        camera = True
        while camera == True:
            success, frame = cap.read()
            
            for code in decode(frame):
                return(str(code.data.decode('utf-8')))
            cv2.imshow('Testing-code-scan', frame)
            cv2.waitKey(1)


def showDrink():
    #Reads the QR code
    price = 0
    drink = readQRFromCamera().strip("']['").split("', '")
    connection = create_server_connection("localhost", "root", "", "QRBucks")

    #Selects the size and returns the price for the drink based on its size
    select = "SELECT " + drink[0] + " FROM Beverages WHERE BeverageName = '" + drink[1] + "'"
    query = read_query(connection, select)
    if query != []:
        query = formatString(str(query[0]))
        price = price + float(query)

    #Selects the drizzle and returns the price for the drizzle. If Default or None, price doesn't change
    select = "SELECT DrizzlePrice FROM Drizzles WHERE DrizzleName = '" + drink[2] + "'"
    query = read_query(connection, select)
    if query != []:
        query = formatString(str(query[0]))
        price = price + float(query)

    #Selects the espresso type and returns the price for the drizzle. If Default or None, price doesn't change
    select = "SELECT EspressoPrice FROM Espresso WHERE EspressoName = '" + drink[3] + "'"
    query = read_query(connection, select)
    if query != []:
        query = formatString(str(query[0]))
        price = price + float(query)

    #Selects the milk type and returns the price for the milk. If Default or None, price doesn't change
    select = "SELECT MilkPrice FROM Milk WHERE MilkName = '" + drink[4] + "'"
    query = read_query(connection, select)
    if query != []:
        query = formatString(str(query[0]))
        price = price + float(query)

    #Selects the syrup type and returns the price for the syrup. If Default or None, price doesn't change
    select = "SELECT SyrupPrice FROM Syrups WHERE SyrupName = '" + drink[5] + "'"
    query = read_query(connection, select)
    if query != []:
        query = formatString(str(query[0]))
        price = price + float(query)

    completedDrink = ""
    for modification in drink:
        if modification != "Default" and modification != "None":
            print(modification)
            completedDrink = completedDrink + " " + modification
    completedDrink = completedDrink + " " + str(price)
    print(price)
    return(completedDrink)



showDrink()

