import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from sympy import *
import numpy as np
from numpy.linalg import inv
from utils.EulerCalc import EulerAngle2Rot
from utils.EndPointCalc import ToolEndCoord


""""
Hand tool Callibration
This App is used to solve an Ax=b problem to achive the callibration
"""

class App:    
    # the default image is used to get the image size and create a canvas
    def __init__(self,window,window_title):  
        # digit precision setting
        np.set_printoptions(precision=4)
        # create A matrix and b matrix
        self.A = np.zeros(shape=(1,3),dtype=float)
        self.b = np.zeros(shape=(1,1),dtype=float)
        self.point_array = np.zeros(shape=(1,3),dtype=float)
        # insert coordinate count
        self.ins_count = 0
        # symbol define
        self.x = Symbol('x')
        self.y = Symbol('y')
        self.z = Symbol('z')

        
        """ window setting initialize """
        self.window = window
        self.window.title(window_title)
        self.window.geometry('500x400')

        # Create Frame 
        self.frm = tk.Frame(self.window).pack()
        self.frm_left = tk.Frame(self.frm)
        self.frm_left.pack(side='left')      # Place the Left-frame on the left side of main-frame

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
        self.entryText = [tk.StringVar() for i in range(6)]     # Create list of EntryText
        self.loop_box = []
        for i in range(6):
            self.loop_box.append(tk.Entry(self.frm_left, width=8, textvariable=self.entryText[i]))
            row_num = 3 if i<3 else 5
            self.loop_box[i].grid(row = row_num, column = i%3 + 1,sticky=tk.NW,padx=35)
                
        # Button
        self.btn_Insert = tk.Button(self.frm_left, text='insert', width=8,
                    height=1, command = self.insert).grid(row=7,pady=40)

        self.btn_Calculate = tk.Button(self.frm_left, text='Calculate', width=8,
                    height=1, command = self.Calculate).grid(row=7,column=1)

        self.btn_Cancel = tk.Button(self.frm_left, text='Cancel', width=8,
                    height=1, command = self.Cancel).grid(row=7,column=2)

        self.window.mainloop()


    # define the action for insert Button        
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
        # and get the value from entrybox
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

        # Calculate the end point coordinate of tool 
        self.R06 = EulerAngle2Rot(self.A_angle, self.B_angle, self.C_angle)
        self.end_coor_of_tool = ToolEndCoord(self.R06,self.X_coor,self.Y_coor,self.Z_coor,self.tool_length)

        # end point coordinate of tool assign to an array
        if self.ins_count == 0:
            self.point_array = np.array(self.end_coor_of_tool[:3].reshape(1,3))
        else:
            self.point_array = np.vstack((self.point_array,self.end_coor_of_tool[:3].reshape(1,3)))

        # ins_count + 1 whenever the inert button click
        self.ins_count += 1
        messagebox.showinfo('Done', 'successfully insert.')
        for i in range(len(self.entryText)):
            self.entryText[i].set('')

    # define the action for Calculate Button        
    def Calculate(self):
        if self.ins_count <=3 :
            messagebox.showerror('Error',' Point is less than 4\n Now is {} !'.format(self.ins_count))
            return

        for i in range(self.ins_count):
            # f = (x-p[0])**2 + (y-p[1])**2 + (z-p[2])**2 - R**2
            globals()['f%s' %i] = (self.x-self.point_array[i][0])**2 + (self.y-self.point_array[i][1])**2 + (self.z-self.point_array[i][2])**2 - self.radius**2
        
        for i in range(self.ins_count-1):
            #res_f = expand(f1-f2)
            globals()['res_f%s' %i] = expand(eval('f'+str(i))-(eval('f'+str(i+1))))

        for i in range(self.ins_count-1):
            # get constant function
            get_const = lambda expr: expr.func(*[var for var in expr.args if not var.free_symbols])

            if i == 0:
                self.A[i][0] = eval("res_f"+str(i)).coeff(self.x)
                self.A[i][1] = eval("res_f"+str(i)).coeff(self.y)
                self.A[i][2] = eval("res_f"+str(i)).coeff(self.z)
                const = get_const(eval("res_f"+str(i)))
                self.b[i][0] = -const    # negative because transposition of term
            else:
                temp_x = eval("res_f"+str(i)).coeff(self.x)
                temp_y = eval("res_f"+str(i)).coeff(self.y)
                temp_z = eval("res_f"+str(i)).coeff(self.z)
                const = get_const(eval("res_f"+str(i)))
                xyz_coor = np.array([temp_x,temp_y,temp_z])
                self.A = np.vstack((self.A,xyz_coor))
                self.b = np.vstack((self.b,-const))
        
        # change object to float type
        self.A = self.A.astype(float)
        self.b = self.b.astype(float)

        # inv(A'A)A'b   
        self.ans = (inv(np.transpose(self.A).dot(self.A)).dot(np.transpose(self.A))).dot(self.b)
        print(self.ans)

    # define the action for Cancel Button        
    def Cancel(self):
        self.window.destroy()


App(tk.Tk(),'My window')