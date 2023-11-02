#!/usr/bin/python
import threading, time, subprocess, logging, minimalmodbus
# from apscheduler.schedulers import Scheduler
from time import sleep
import serial

import re
import tkinter as tk
from tkinter import ttk




class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def settings(self):
        instrument = minimalmodbus.Instrument("/dev/ttyUSB0", 1)

        instrument.serial.baudrate = 9600  # Baud
        instrument.serial.bytesize = 8
        instrument.serial.parity = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 0.05  # seconds

        instrument.address = 1  # this is the slave address number
        instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
        instrument.clear_buffers_before_each_transaction = True

        # wattson = minimalmodbus.Instrument("/dev/ttyUSB0", 1)
        # wattson = minimalmodbus.Instrument("/dev/ttyUSB0", 1, debug=True)


        #TEC = instrument.read_float(12,functioncode=4)  # total energy consumed KWh
        TEC = instrument.read_float(0,functioncode=4)  # total energy consumed KWh

        print(TEC)

        


        while True:
                 sleep(1)
                 print(TEC)



