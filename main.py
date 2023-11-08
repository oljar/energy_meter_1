import re
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from Model import Model
from View import View
import View as V
import threading


class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        # create a model


mod_1_adr_var = tk.StringVar()
dev_1_adr_var = tk.StringVar()
mod_2_adr_var = tk.StringVar()
dev_2_adr_var = tk.StringVar()
mod_3_adr_var = tk.StringVar()
dev_3_adr_var = tk.StringVar()
mod_4_adr_var = tk.StringVar()
dev_4_adr_var = tk.StringVar()
mod_5_adr_var = tk.StringVar()
dev_5_adr_var = tk.StringVar()
mod_6_adr_var = tk.StringVar()
dev_6_adr_var = tk.StringVar()
mod_7_adr_var = tk.StringVar()
dev_7_adr_var = tk.StringVar()
mod_8_adr_var = tk.StringVar()
dev_8_adr_var = tk.StringVar()
mod_9_adr_var = tk.StringVar()
dev_9_adr_var = tk.StringVar()
mod_10_adr_var = tk.StringVar()
dev_10_adr_var = tk.StringVar()
t = tk.StringVar()
delta_t = tk.StringVar()
save_control = tk.BooleanVar()

data_1 = tk.StringVar()
data_2 = tk.StringVar()
data_3 = tk.StringVar()
data_4 = tk.StringVar()
data_5 = tk.StringVar()
data_6 = tk.StringVar()
data_7 = tk.StringVar()
data_8 = tk.StringVar()
data_9 = tk.StringVar()
data_10 = tk.StringVar()

model = Model(save_control,t, delta_t, mod_1_adr_var, dev_1_adr_var, mod_2_adr_var, dev_2_adr_var, mod_3_adr_var, dev_3_adr_var,
              mod_4_adr_var, dev_4_adr_var, mod_5_adr_var, dev_5_adr_var, mod_6_adr_var, dev_6_adr_var, mod_7_adr_var,
              dev_7_adr_var, mod_8_adr_var, dev_8_adr_var, mod_9_adr_var, dev_9_adr_var, mod_10_adr_var, dev_10_adr_var,
              data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10)

view = View(V.window)

controller = Controller(model, view)
view.set_controller(controller)

V.tab_parent.add(V.tab0, text='settings')
V.tab_parent.add(V.tab1, text='identification')

V.tab_parent.pack(expand=1, fill='both')

app = Application(V.window)
# check
# controller.settings()
# controller.make()
V.window.mainloop()

# set the controller to view
