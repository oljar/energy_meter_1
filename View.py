import re
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from Model import Model


window = tk.Tk()
window.title("EVOT_printer")
window.geometry('1000x1000')

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





        self.dist = ttk.Label(tab0, width=5)
        self.dist.grid(row=0, column=0)

        self.labelframe01 = tk.LabelFrame(tab0, text="")
        self.labelframe01.grid(row = 1, column =1, sticky=tk.NSEW)


#######################################################################################################################



        self.label = ttk.Label(self.labelframe01, text='Wykres 01 - adres modbus')
        self.label.grid(row=6, column=2)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=1, column=0)

        self.mod_1_adr_entry = ttk.Entry(self.labelframe01, textvariable = self.mod_1_adr_var)
        self.mod_1_adr_entry.grid(row=6, column=3)

        self.mod_1_adr_entry.insert(0, "0")

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=6, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=6, column=5)

        self.dev_1_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_1_adr_var)
        self.dev_1_adr_entry.grid(row=6,column=6)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=7, column=0)

        self.dev_1_adr_entry.insert(0, "1")



        ########################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Wykres 02 - adres modbus')
        self.label.grid(row=10, column=2)

        self.mod_2_adr_entry = ttk.Entry(self.labelframe01, textvariable = self.mod_2_adr_var)
        self.mod_2_adr_entry.grid(row=10, column=3)

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=10, column=4)

        self.mod_2_adr_entry.insert(0, "6")


        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=10, column=5)

        self.dev_2_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_2_adr_var)
        self.dev_2_adr_entry.grid(row=10,column=6)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=11, column=0)

        self.dev_2_adr_entry.insert(0, "1")
        #######################################################################################################################

        self.label = ttk.Label(self.labelframe01, text='Wykres 03 - adres modbus')
        self.label.grid(row=15, column=2)

        self.mod_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_3_adr_var)
        self.mod_3_adr_entry.grid(row=15, column=3)

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=15, column=4)

        self.mod_3_adr_entry.insert(0, "12")

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=15, column=5)

        self.dev_3_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_3_adr_var)
        self.dev_3_adr_entry.grid(row=15, column=6)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=16, column=0)

        self.dev_3_adr_entry.insert(0, "1")

        #######################################################################################################################
        self.label = ttk.Label(self.labelframe01, text='Wykres 04 - adres modbus')
        self.label.grid(row=20, column=2)

        self.mod_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.mod_4_adr_var)
        self.mod_4_adr_entry.grid(row=20, column=3)

        self.dist = ttk.Label(self.labelframe01, width=5)
        self.dist.grid(row=20, column=4)

        self.label = ttk.Label(self.labelframe01, text='adres urządzenia')
        self.label.grid(row=20, column=5)

        self.mod_4_adr_entry.insert(0, "70")

        self.dev_4_adr_entry = ttk.Entry(self.labelframe01, textvariable=self.dev_4_adr_var)
        self.dev_4_adr_entry.grid(row=20, column=6)

        self.dist = ttk.Label(self.labelframe01)
        self.dist.grid(row=21, column=0)

        self.draw_window_button = ttk.Button(self.labelframe01, text= "wykresy",width=5, command= self.draw_chart)
        self.draw_window_button.grid(columnspan=7,sticky = tk.W+tk.E)

        self.dev_4_adr_entry.insert(0, "1")


        ###########################################################################################################################
        self.dist = ttk.Label(tab0, width=5)
        self.dist.grid(row=1, column=0)

        self.labelframe01 = tk.LabelFrame(tab0, text="wykres-2")
        self.labelframe01.grid(row=2, column=1, sticky=tk.NSEW)



    def draw_chart(self):
        self.controller.draw_chart()





        # # email entry
        # self.email_var = tk.StringVar()
        # self.email_entry = ttk.Entry(tab0, textvariable=self.email_var, width=30)
        # self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)
        #
        # self.email_var1 = tk.StringVar()
        # self.email_entry1 = ttk.Entry(tab1, textvariable=self.email_var1, width=30)
        # self.email_entry1.grid(row=2, column=1, sticky=tk.NSEW)
        #
        # # save button
        # self.save_button = ttk.Button(tab0, text='Save', command=self.save_button_clicked)
        # self.save_button.grid(row=1, column=3, padx=10)
        #
        # # message
        # self.message_label = ttk.Label(self, text='', foreground='red')
        # self.message_label.grid(row=2, column=1, sticky=tk.W)
        #
        # # set the controller
        # self.controller = None

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

