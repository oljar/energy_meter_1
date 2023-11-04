import re
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from Model import Model
from View import View
import View as V




class Application(tk.Frame):
        def __init__(self, master):
            super(Application, self).__init__(master)


                # create a model
model = Model('')


view = View(V.window)


controller = Controller(model, view)
controller.settings()
controller.execut()

# set the controller to view
view.set_controller(controller)



V.tab_parent.add(V.tab0,text = 'settings')
V.tab_parent.add(V.tab1,text = 'identification')

V.tab_parent.pack(expand = 1, fill = 'both')

app =Application(V.window)



#check

V.window.mainloop()
