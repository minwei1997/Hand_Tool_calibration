import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk

import numpy as np


class App:    
    # the default image is used to get the image size and create a canvas
    def __init__(self,window,window_title):  
        # create A matrix and b matrix
        A = np.zeros(shape=(1,3))
        b = np.zeros(shape=(1,1))

        
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
        self.Label_Threshold = tk.Label(self.frm_left,text='Tool length : ',font = ('Times',14)).grid(row = 1,sticky=tk.W,pady=35)
        self.Label_J6 = tk.Label(self.frm_left,text = 'J6 :',font = ('Times',14)).grid(row=3)
        # Label for  (X, Y, Z, A, B, C)
        label_list = ['X','Y','Z','A','B','C']
        self.loop_label = []
        for i in range(6):
            self.loop_label.append(tk.Label(self.frm_left, text = label_list[i]))
            if i <3:
                self.loop_label[i].grid(row = 2,column = i+1,sticky=tk.NW,padx=35)
            else:
                self.loop_label[i].grid(row = 4,column = i-3+1,sticky=tk.NW,padx=35)
   
        # Entry
        self.var_radius = tk.StringVar()       # Radius's text Variable
        self.Entry_radius = tk.Entry(self.frm_left,width=8,textvariable=self.var_radius)    # Radius entry
        self.Entry_radius.grid(row = 0,column = 1,sticky=tk.W,padx=35) 

        self.var_tool_length = tk.StringVar()       # Tool length's text Variable
        self.Entry_tool_length = tk.Entry(self.frm_left,width=8,textvariable=self.var_tool_length)     # Tool Length entry
        self.Entry_tool_length.grid(row = 1,column = 1,sticky=tk.W,padx=35) 
        # EntryBox for  (X, Y, Z, A, B, C)
        self.loop_box = []
        J6_var = locals()
        for i in range(6):
            J6_var['J6_var_{}'.format(i)] = tk.StringVar()
            self.loop_box.append(tk.Entry(self.frm_left, width=8,textvariable=eval('J6_var_'+str(i))))
            if i<3:
                self.loop_box[i].grid(row = 3,column = i+1,sticky=tk.NW,padx=35)
            else:
                self.loop_box[i].grid(row = 5,column = i-3+1,sticky=tk.NW,padx=35)

        #Button
        self.btn_Insert = tk.Button(self.frm_left, text='insert', width=8,
                    height=1, command = self.insert).grid(row=7,pady=40)

        self.btn_Calculate = tk.Button(self.frm_left, text='Calculate', width=8,
                    height=1, command = self.Calculate).grid(row=7,column=1)

        self.btn_Cancel = tk.Button(self.frm_left, text='Cancel', width=8,
                    height=1, command = self.Cancel).grid(row=7,column=2)

        self.window.mainloop()


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