#!/usr/bin/python
import threading, time, subprocess, logging, minimalmodbus
# from apscheduler.schedulers import Scheduler
from time import sleep
import serial

import re
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections




class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def my_function(self):
        self.cpu.popleft()
        self.cpu.append(psutil.cpu_percent(interval=1))
        self.ram.popleft()
        self.ram.append(psutil.virtual_memory().percent)



    def animate(self,i):
        self.my_function()
        self.ax.clear()
        self.ax1.clear()
        self.ax.plot(self.cpu)
        #ax.scatter(len(cpu)-1, cpu[-1])
        #ax.text(len(cpu)-1, cpu[-1]+2, f"{cpu[-1]}%")
        self.ax.set_ylim(0,100)
        self.ax1.plot(self.ram)
        #ax1.scatter(len(ram)-1, ram[-1])
        #ax1.text(len(ram)-1, ram[-1]+2, f"{ram[-1]}%")
        self.ax1.set_ylim(0,100)



    def settings(self):
        #instrument = minimalmodbus.Instrument("/dev/ttyUSB0", 1)
        instrument = minimalmodbus.Instrument('com6', 1)

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


        sleep(1)
        print(TEC)

    def execut(self):
        self.cpu = collections.deque(np.zeros(10))
        self.ram = collections.deque(np.zeros(10))
        self.fig = plt.figure(figsize=(10, 5), facecolor='#DEDEDE')
        self.ax = plt.subplot(121)
        self.ax1 = plt.subplot(122)
        self.ax.set_facecolor('#DEDEDE')
        self.ax1.set_facecolor('#DEDEDE')
        ani = FuncAnimation(self.fig, self.animate, interval=100)

        plt.show()




