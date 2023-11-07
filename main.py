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

model = Model(mod_1_adr_var, dev_1_adr_var, mod_2_adr_var, dev_2_adr_var, mod_3_adr_var, dev_3_adr_var, mod_4_adr_var
              , dev_4_adr_var, mod_5_adr_var, dev_5_adr_var, mod_6_adr_var, dev_6_adr_var, mod_7_adr_var, dev_7_adr_var,
              mod_8_adr_var, dev_8_adr_var, mod_9_adr_var, dev_9_adr_var, mod_10_adr_var, dev_10_adr_var)

view = View(V.window)

controller = Controller(model, view)
view.set_controller(controller)

V.tab_parent.add(V.tab0, text='settings')
V.tab_parent.add(V.tab1, text='identification')

V.tab_parent.pack(expand=1, fill='both')

app = Application(V.window)

# check
#controller.settings()
#controller.make()
V.window.mainloop()






# set the controller to view

