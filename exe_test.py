import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

import numpy as np


class App:    
    # the default image is used to get the image size and create a canvas
    def __init__(self,window,window_title):          
        """ window setting initialize """
        self.window = window
        self.window.title(window_title)
        self.window.geometry('800x550')

        # Create Frame 
        self.frm = tk.Frame(self.window).pack()
        self.frm_left = tk.Frame(self.frm)
        self.frm_right = tk.Frame(self.frm)
        self.frm_left.pack(side='left')      # Place the Left-frame on the left side of main-frame
        self.frm_right.pack(side='right')    # Place the Right-frame on the right side of main-frame

        # Create a canvas
        self.canvas = tk.Canvas(self.frm_right, bg='pink', height=600, width=500)
        self.canvas.pack()

        # Label
        self.Label_radius = tk.Label(self.frm_left,text='Radius : ', font = ('Times',14)).grid(row = 0)



    def insert(self):
        # check if some entrybox are empty
        if len(self.loop_box[0].get()) != 0 and len(self.loop_box[1].get()) != 0 and len(self.loop_box[2].get()) != 0 \
            and len(self.loop_box[3].get()) != 0 and len(self.loop_box[4].get()) != 0 and len(self.loop_box[5].get()) != 0 \
            and len(self.var_radius.get()) != 0 and len(self.var_tool_length.get()) != 0:
            pass
        else:
            messagebox.showerror('Error','Some entrybox are empty !')
            return

        # check if all entrybox are float type
        try :
            self.radius = float(self.var_radius.get())
            self.tool_length = float(self.var_tool_length.get())
            self.X_coor = float(self.loop_box[0].get())
            self.Y_coor = float(self.loop_box[1].get())
            self.Z_coor = float(self.loop_box[2].get())
            self.A_angle = float(self.loop_box[3].get())
            self.B_angle = float(self.loop_box[4].get())
            self.C_angle = float(self.loop_box[5].get())
        except :
            messagebox.showerror('Error','Some entrybox type are not right.\nPlease retry again !')
            return

        ######################


    def Calculate(self):
        # get the label & path text from entrybox (and check if the entrybox is empty)
        if len(self.loop_box[0].get()) != 0 :
            self.label = self.var_radius.get()
            self.process_img_path = self.var_path_read.get() + '/'
            self.out_file = self.var_path_save.get() + '/'
        else :
            messagebox.showerror('Error','Some entrybox are empty !')
            return

        # get the Threshold text from Threshold entrybox and check if the Threshold is an integer
        try :
            self.perimeter_threshold = int(self.var_Threshold.get())
        except :
            messagebox.showerror('Error','Threshold is not an integer.\nPlease retry again !')
            return

        # get the Image type form combobox and check if you have select a image type
        if self.type_var.get() != '' :
            self.img_type = self.type_var.get()
        else:
            messagebox.showerror('Error','You have not select a  image type yet !')
            return


            
    def Cancel(self):
        self.window.destroy()



App(tk.Tk(),'My window')