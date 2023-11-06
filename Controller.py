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
import time


class Controller:
    def __init__(self, model, view):
        self.parameter = tk.StringVar()
        self.model = model
        self.view = view
        self.model.mod_1_adr_var= tk.StringVar()






        self.t1 = time.time()
        self.fig = plt.figure(figsize=(10, 5), facecolor='#DEDEDE')

        self.time_s = collections.deque(np.zeros(10))
        self.param_1 = collections.deque(np.zeros(10))
        self.param_2 = collections.deque(np.zeros(10))
        self.param_3 = collections.deque(np.zeros(10))
        self.param_4 = collections.deque(np.zeros(10))
###
        self.ax = plt.subplot(221) ### set window position
        self.ax_co = self.ax.twiny()

        self.ax2 = plt.subplot(222)  ### set window position
        self.ax2_co = self.ax.twiny()


        self.ax3 = plt.subplot(223)     ### set window position
        self.ax3_co = self.ax.twiny()

        self.ax4 = plt.subplot(224)     ### set window position
        self.ax4_co = self.ax.twiny()

        self.ax5 = plt.subplot(224)  ### set window position
        self.ax5_co = self.ax.twiny()

        self.ax6 = plt.subplot(224)  ### set window position
        self.ax6_co = self.ax.twiny()










    def my_function(self):
        self.time_s.popleft()
        self.time_s.append(self.delta_t)



#  modbus settings

        def chart1_myfunction():
            self.instrument.address = int(self.model.dev_1_adr_var.get())
            self.param_1.append(self.instrument.read_float(int(self.model.mod_1_adr_var.get()), functioncode=4))  #adress modbus
            self.param_1.popleft()
        chart1_myfunction()

        def chart2_myfunction():
            self.instrument.address = int(self.model.dev_2_adr_var.get())
            self.param_2.append(self.instrument.read_float(int(self.model.mod_2_adr_var.get()), functioncode=4))  #adress modbus
            self.param_2.popleft()
        chart2_myfunction()

        def chart3_myfunction():
            self.instrument.address = int(self.model.dev_3_adr_var.get())
            self.param_3.append(self.instrument.read_float(int(self.model.mod_3_adr_var.get()), functioncode=4))  # adress modbus
            self.param_3.popleft()
        chart3_myfunction()

        def chart4_myfunction():
            self.instrument.address = int(self.model.dev_4_adr_var.get())
            self.param_4.append(self.instrument.read_float(int(self.model.mod_4_adr_var.get()), functioncode=4))  # adress modbus
            self.param_4.popleft()
        chart4_myfunction()
##########################################################################################################################################
        def chart5_myfunction():
            self.instrument.address = int(self.model.dev_1_adr_var.get())
            self.param_1.append(
                self.instrument.read_float(int(self.model.mod_1_adr_var.get()), functioncode=4))  # adress modbus
            self.param_1.popleft()

        chart5_myfunction()

        def chart6_myfunction():
            self.instrument.address = int(self.model.dev_2_adr_var.get())
            self.param_2.append(
                self.instrument.read_float(int(self.model.mod_2_adr_var.get()), functioncode=4))  # adress modbus
            self.param_2.popleft()

        chart6_myfunction()

        def chart7_myfunction():
            self.instrument.address = int(self.model.dev_3_adr_var.get())
            self.param_3.append(
                self.instrument.read_float(int(self.model.mod_3_adr_var.get()), functioncode=4))  # adress modbus
            self.param_3.popleft()

        chart7_myfunction()

        def chart8_myfunction():
            self.instrument.address = int(self.model.dev_4_adr_var.get())
            self.param_4.append(
                self.instrument.read_float(int(self.model.mod_4_adr_var.get()), functioncode=4))  # adress modbus
            self.param_4.popleft()

        chart8_myfunction()






    def animate(self, i):
        self.t2 = time.time()
        self.delta_t = (self.t2 - self.t1)
        self.my_function()

        def chart1_animate(i):

            self.ax.clear()
            self.ax.plot(self.time_s, self.param_1)
            self.ax.scatter(self.time_s[-1], self.param_1[-1])
            self.ax.text(self.time_s[-1], self.param_1[-1], f"{self.param_1[-1]}")
            self.ax.set_ylim(-1, self.param_1[-1]+0.1*self.param_1[-1]+3)
            self.ax_co.set_xlim(0, 10)
            self.ax.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)

        chart1_animate(i)

        def chart2_animate(i):

            self.ax2.clear()
            self.ax2.plot(self.time_s, self.param_2)
            self.ax2.scatter(self.time_s[-1], self.param_2[-1])
            self.ax2.text(self.time_s[-1], self.param_2[-1], f"{self.param_2[-1]}")
            self.ax2.set_ylim(-1, self.param_2[-1]+0.1*self.param_2[-1]+3)
            self.ax2_co.set_xlim(0, 10)
            self.ax2.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart2_animate(i)

        def chart3_animate(i):

            self.ax3.clear()
            self.ax3.plot(self.time_s, self.param_3)
            self.ax3.scatter(self.time_s[-1], self.param_3[-1])
            self.ax3.text(self.time_s[-1], self.param_3[-1], f"{self.param_3[-1]}")
            self.ax3.set_ylim(-1, self.param_3[-1]+0.1*self.param_3[-1]+3)
            self.ax3_co.set_xlim(0, 10)
            self.ax3.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart3_animate(i)


        def chart4_animate(i):

            self.ax4.clear()
            self.ax4.plot(self.time_s, self.param_4)
            self.ax4.scatter(self.time_s[-1], self.param_4[-1])
            self.ax4.text(self.time_s[-1], self.param_4[-1], f"{self.param_4[-1]}")
            self.ax4.set_ylim(-1, self.param_4[-1]+0.1*self.param_4[-1]+3)
            self.ax4_co.set_xlim(0, 10)
            self.ax4.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart4_animate(i)

        def chart5_animate(i):
            self.ax5.clear()
            self.ax5.plot(self.time_s, self.param_1)
            self.ax5.scatter(self.time_s[-1], self.param_1[-1])
            self.ax5.text(self.time_s[-1], self.param_1[-1], f"{self.param_1[-1]}")
            self.ax5.set_ylim(-1, self.param_1[-1] + 0.1 * self.param_1[-1] + 3)
            self.ax5_co.set_xlim(0, 10)
            self.ax5.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart5_animate(i)

        def chart6_animate(i):
            self.ax6.clear()
            self.ax6.plot(self.time_s, self.param_2)
            self.ax6.scatter(self.time_s[-1], self.param_2[-1])
            self.ax6.text(self.time_s[-1], self.param_2[-1], f"{self.param_2[-1]}")
            self.ax6.set_ylim(-1, self.param_2[-1] + 0.1 * self.param_2[-1] + 3)
            self.ax6_co.set_xlim(0, 10)
            self.ax6.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart6_animate(i)

        def chart7_animate(i):
            self.ax7.clear()
            self.ax7.plot(self.time_s, self.param_3)
            self.ax7.scatter(self.time_s[-1], self.param_3[-1])
            self.ax7.text(self.time_s[-1], self.param_3[-1], f"{self.param_3[-1]}")
            self.ax7.set_ylim(-1, self.param_3[-1] + 0.1 * self.param_3[-1] + 3)
            self.ax7_co.set_xlim(0, 10)
            self.ax7.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart7_animate(i)

        def chart8_animate(i):
            self.ax8.clear()
            self.ax8.plot(self.time_s, self.param_4)
            self.ax8.scatter(self.time_s[-1], self.param_4[-1])
            self.ax8.text(self.time_s[-1], self.param_4[-1], f"{self.param_4[-1]}")
            self.ax8.set_ylim(-1, self.param_4[-1] + 0.1 * self.param_4[-1] + 3)
            self.ax8_co.set_xlim(0, 10)
            self.ax8.set_xlim(right=int(self.delta_t) - 10, left=int(self.delta_t) + 1)
        chart8_animate(i)

    def make(self):


        def chart1_make():

            self.ax.set_xlim(0, -10)
            self.ax.set_facecolor('#DEDEDE')
            self.ax_co.set_xlim(0, 10)
        chart1_make()


        def chart2_make():
            self.ax2.set_xlim(0, -10)
            self.ax2.set_facecolor('#DEDEDE')
            self.ax2_co.set_xlim(0, 10)
        chart2_make()

        def chart3_make():
            self.ax3.set_xlim(0, -10)
            self.ax3.set_facecolor('#DEDEDE')
            self.ax3_co.set_xlim(0, 10)
        chart3_make()

        def chart4_make():
            self.ax4.set_xlim(0, -10)
            self.ax4.set_facecolor('#DEDEDE')
            self.ax4_co.set_xlim(0, 10)
        chart4_make()

        ani = FuncAnimation(self.fig, self.animate, interval=1000, cache_frame_data=False,repeat=True)
        plt.show()






    def settings(self):
        # instrument = minimalmodbus.Instrument("/dev/ttyUSB0", 1)
        self.instrument = minimalmodbus.Instrument('com6', 1)
        self.instrument.serial.baudrate = 9600  # Baud
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 0.05  # seconds
        self.instrument.address = 1  # this is the slave address number
        self.instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
        self.instrument.clear_buffers_before_each_transaction = True

    def draw_chart(self):
        self.model.mod_1_adr_var.set(self.view.mod_1_adr_var.get())
        self.model.dev_1_adr_var.set(self.view.dev_1_adr_var.get())

        self.model.mod_2_adr_var.set(self.view.mod_2_adr_var.get())
        self.model.dev_2_adr_var.set(self.view.dev_2_adr_var.get())

        self.model.mod_3_adr_var.set(self.view.mod_3_adr_var.get())
        self.model.dev_3_adr_var.set(self.view.dev_3_adr_var.get())

        self.model.mod_4_adr_var.set(self.view.mod_4_adr_var.get())
        self.model.dev_4_adr_var.set(self.view.dev_4_adr_var.get())



        print(self.model.mod_1_adr_var.get())
        self.settings()
        self.make()