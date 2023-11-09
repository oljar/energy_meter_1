import re
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from Model import Model
import time
window = tk.Tk()

window.title("EVOT_printer")
window.geometry('670x550')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)



class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.dev_1_adr_var = tk.StringVar()
        self.mod_1_adr_var = tk.StringVar()

        self.dev_2_adr_var = tk.StringVar()
        self.mod_2_adr_var = tk.StringVar()

        self.dev_3_adr_var = tk.StringVar()
        self.mod_3_adr_var = tk.StringVar()

        self.dev_4_adr_var = tk.StringVar()
        self.mod_4_adr_var = tk.StringVar()

        self.dev_5_adr_var = tk.StringVar()
        self.mod_5_adr_var = tk.StringVar()

        self.dev_6_adr_var = tk.StringVar()
        self.mod_6_adr_var = tk.StringVar()

        self.dev_7_adr_var = tk.StringVar()
        self.mod_7_adr_var = tk.StringVar()

        self.dev_8_adr_var = tk.StringVar()
        self.mod_8_adr_var = tk.StringVar()

        self.dev_9_adr_var = tk.StringVar()
        self.mod_9_adr_var = tk.StringVar()

        self.dev_10_adr_var = tk.StringVar()
        self.mod_10_adr_var = tk.StringVar()

        self.dist = ttk.Label(tab0, width=5)
        self.dist.grid(row=0, column=0)

        self.labelframe01 = tk.LabelFrame(tab0, text="")
        self.labelframe01.grid(row=1, column=1, sticky=tk.NSEW)

        self.stop_check = tk.BooleanVar()



        #######################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 01 - adres modbus')
        self.label.grid(row=6, column=2)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=1, column=0)

        self.mod_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_1_adr_var)
        self.mod_1_adr_entry.grid(row=6, column=3)

        self.mod_1_adr_entry.insert(0, "0")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=6, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=6, column=5)

        self.dev_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_1_adr_var)
        self.dev_1_adr_entry.grid(row=6, column=6)
        self.dev_1_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=7, column=0)

        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 02 - adres modbus')
        self.label.grid(row=10, column=2)

        self.mod_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_2_adr_var)
        self.mod_2_adr_entry.grid(row=10, column=3)

        self.mod_2_adr_entry.insert(0, "6")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=10, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=10, column=5)

        self.dev_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_2_adr_var)
        self.dev_2_adr_entry.grid(row=10, column=6)
        self.dev_2_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=11, column=0)

        #######################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 03 - adres modbus')
        self.label.grid(row=15, column=2)

        self.mod_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_3_adr_var)
        self.mod_3_adr_entry.grid(row=15, column=3)
        self.mod_3_adr_entry.insert(0, "12")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=15, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=15, column=5)

        self.dev_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_3_adr_var)
        self.dev_3_adr_entry.grid(row=15, column=6)
        self.dev_3_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=16, column=0)

        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='Zapis/Wykres 04 - adres modbus')
        self.label.grid(row=20, column=2)

        self.mod_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_4_adr_var)
        self.mod_4_adr_entry.grid(row=20, column=3)

        self.mod_4_adr_entry.insert(0, "70")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=20, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=20, column=5)

        self.dev_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_4_adr_var)
        self.dev_4_adr_entry.grid(row=20, column=6)
        self.dev_4_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=21, column=0)

        ###########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 05 - adres modbus')
        self.label.grid(row=30, column=2)

        self.mod_5_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_5_adr_var)
        self.mod_5_adr_entry.grid(row=30, column=3)
        self.mod_5_adr_entry.insert(0, "70")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=30, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=30, column=5)

        self.dev_5_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_5_adr_var)
        self.dev_5_adr_entry.grid(row=30, column=6)
        self.dev_5_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=31, column=0)
        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 06 - adres modbus')
        self.label.grid(row=40, column=2)

        self.mod_6_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_6_adr_var)
        self.mod_6_adr_entry.grid(row=40, column=3)
        self.mod_6_adr_entry.insert(0, "70")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=40, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=40, column=5)

        self.dev_6_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_6_adr_var)
        self.dev_6_adr_entry.grid(row=40, column=6)
        self.dev_6_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=41, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 07 - adres modbus')
        self.label.grid(row=50, column=2)

        self.mod_7_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_7_adr_var)
        self.mod_7_adr_entry.grid(row=50, column=3)

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=50, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=50, column=5)

        self.mod_7_adr_entry.insert(0, "70")

        self.dev_7_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_7_adr_var)
        self.dev_7_adr_entry.grid(row=50, column=6)

        self.dev_7_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=51, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 08 - adres modbus')
        self.label.grid(row=60, column=2)

        self.mod_8_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_8_adr_var)
        self.mod_8_adr_entry.grid(row=60, column=3)
        self.mod_8_adr_entry.insert(0, "70")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=60, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=60, column=5)

        self.dev_8_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_8_adr_var)
        self.dev_8_adr_entry.grid(row=60, column=6)

        self.dev_8_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=61, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 09 - adres modbus')
        self.label.grid(row=70, column=2)

        self.mod_9_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_9_adr_var)
        self.mod_9_adr_entry.grid(row=70, column=3)
        self.mod_9_adr_entry.insert(0, "70")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=70, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=70, column=5)

        self.dev_9_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_9_adr_var)
        self.dev_9_adr_entry.grid(row=70, column=6)
        self.dev_9_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=71, column=0)

        ############################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Zapis 10 - adres modbus')
        self.label.grid(row=80, column=2)

        self.mod_10_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_10_adr_var)
        self.mod_10_adr_entry.grid(row=80, column=3)
        self.mod_10_adr_entry.insert(0, "70")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=80, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=80, column=5)

        self.dev_10_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_10_adr_var)
        self.dev_10_adr_entry.grid(row=80, column=6)
        self.dev_10_adr_entry.insert(0, "1")

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=81, column=0)

        ############################################################################################################################

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=31, column=0)

        ###########################################################################################################################

        self.draw_window_button = ttk.Button(self.labelframe01, text="wykresy", width=5, command=self.draw_chart)
        self.draw_window_button.grid(row=90, columnspan=7, sticky=tk.W + tk.E)

        ###########################################################################################################################

        self.start_save_button = ttk.Button(self.labelframe01, text="start -zapis", width=2, command=self.start_save)
        self.start_save_button.grid(row=91, column=3, ipadx=50)

        ##########################################################################################################################


        self.stop_save_button = ttk.Button(self.labelframe01, text="stop - zapis", width=2, command=self.stop_save)
        self.stop_save_button.grid(row=91, column=5, ipadx=50)

        self.dist = ttk.Label(tab0, width=5)
        self.dist.grid(row=1, column=0)

        self.labelframe01 = tk.LabelFrame(tab0, text="wykres-2")
        self.labelframe01.grid(row=2, column=1, sticky=tk.NSEW)

    def draw_chart(self):
        self.controller.settings()
        self.controller.transfer_data()
        self.controller.make()


    def start_save(self):
        self.stop_check.set(False)
        self.controller.settings()
        self.controller.transfer_data()
        #
        self.controller.start_save()
        self.start_loop()




    def start_loop(self):
        time.sleep(0.1)
        self.controller.save_data()
        if self.stop_check.get() :
            return
        self.labelframe01.after(1000, self.start_loop)




        # self.start_save_button.config(state= "disabled")
        # self.stop_save_button.config(state = "enabled")

    def stop_save(self):

        self.stop_check.set(True)

        # self.start_save_button.config(state="enabled")
        # self.stop_save_button.config(state="disabled")

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
