#----------------- `Library` ---------------
import tkinter
from tkinter import *
from tkinter import messagebox, messagebox
import math
from PIL import ImageTk, Image  # For import image
import time
print("hello")

#----------------- `Create App` ---------------

Calcu = Tk()
Calcu.title('Graphic Calculator')
Calcu.geometry('447x590')



Enter_Text = StringVar()
Operation_Text = StringVar()
Other_Text = StringVar()

#----------------- `Import The Images of the buttons` ---------------

Pic_0_C1 = PhotoImage(file = 'Button_0_C1.png')
Pic_0_C2 = PhotoImage(file = 'Button_0_C2.png') # Number 0

Pic_1_C1 = PhotoImage(file = 'Button_1_C1.png')
Pic_1_C2 = PhotoImage(file = 'Button_1_C2.png') # Number 1

Pic_2_C1 = PhotoImage(file = 'Button_2_C1.png')
Pic_2_C2 = PhotoImage(file = 'Button_2_C2.png') # Number 2

Pic_3_C1 = PhotoImage(file = 'Button_3_C1.png')
Pic_3_C2 = PhotoImage(file = 'Button_3_C2.png') # Number 3

Pic_4_C1 = PhotoImage(file = 'Button_4_C1.png')
Pic_4_C2 = PhotoImage(file = 'Button_4_C2.png') # Number 4

Pic_5_C1 = PhotoImage(file = 'Button_5_C1.png')
Pic_5_C2 = PhotoImage(file = 'Button_5_C2.png') # Number 5

Pic_6_C1 = PhotoImage(file = 'Button_6_C1.png')
Pic_6_C2 = PhotoImage(file = 'Button_6_C2.png') # Number 6

Pic_7_C1 = PhotoImage(file = 'Button_7_C1.png')
Pic_7_C2 = PhotoImage(file = 'Button_7_C2.png') # Number 7

Pic_8_C1 = PhotoImage(file = 'Button_8_C1.png')
Pic_8_C2 = PhotoImage(file = 'Button_8_C2.png') # Number 8

Pic_9_C1 = PhotoImage(file = 'Button_9_C1.png')
Pic_9_C2 = PhotoImage(file = 'Button_9_C2.png') # Number 9

Pic_Point_C1 = PhotoImage(file = 'Button_P_C1.png')
Pic_Point_C2 = PhotoImage(file = 'Button_P_C2.png') # Point `.`

Pic_Subtraction_C1 = PhotoImage(file = 'Button_Subtraction_C1.png')
Pic_Subtraction_C2 = PhotoImage(file = 'Button_Subtraction_C2.png') # Button `-`

Pic_Plus_C1 = PhotoImage(file = 'Button_+_C1.png')
Pic_Plus_C2 = PhotoImage(file = 'Button_+_C2.png') # Button `+`

Pic_D_C1 = PhotoImage(file = 'Button_D_C1.png')
Pic_D_C2 = PhotoImage(file = 'Button_D_C2.png') # Button `➗`

Pic_X_C1 = PhotoImage(file = 'Button_X_C1.png')
Pic_X_C2 = PhotoImage(file = 'Button_X_C2.png') # Button `X`

Pic_Answer_C1 = PhotoImage(file = 'Button_=_C1.png')
Pic_Answer_C2 = PhotoImage(file = 'Button_=_C2.png') # Button `=`

Pic_R_C1 = PhotoImage(file = 'Button_R_C1.png')
Pic_R_C2 = PhotoImage(file = 'Button_R_C2.png') # Button `√`

Pic_D2_C1 = PhotoImage(file = 'Button_D2_C1.png')
Pic_D2_C2 = PhotoImage(file = 'Button_D2_C2.png') # Button `%`

Pic_C_C1 = PhotoImage(file = 'Button_C_C1.png')
Pic_C_C2 = PhotoImage(file = 'Button_C_C2.png') # Button `C` => clear!

Pic_E_C1 = PhotoImage(file = 'Button_E_C1.png')
Pic_E_C2 = PhotoImage(file = 'Button_E_C2.png') # Button `E` => exit!

#----------------- `def` ---------------
def Answer() :
  Operation = Operation_Text.get()

  if Operation == '√' :
    T1 = float(Enter_Text.get())
    Other_Text.set('')
    Enter_Text.set(str(math.sqrt(T1)))
    Operation_Text.set('')

  elif Other_Text.get() != '' :
    if Enter_Text.get() != '' :
      if Operation == '➗' :

        T1 = float(Enter_Text.get())
        T2 = float(Other_Text.get())
        Other_Text.set('')
        Enter_Text.set(str(T1/T2))
        Operation_Text.set('')
      elif Operation == '%' :

        T1 = float(Enter_Text.get())
        T2 = float(Other_Text.get())
        Other_Text.set('')
        Enter_Text.set(str(T1%T2))
        Operation_Text.set('')
      elif Operation == 'x' :

        T1 = float(Enter_Text.get())
        T2 = float(Other_Text.get())
        Other_Text.set('')
        Enter_Text.set(str(T1*T2))
        Operation_Text.set('')
      elif Operation == '-' :

        T1 = float(Enter_Text.get())
        T2 = float(Other_Text.get())
        Other_Text.set('')
        Enter_Text.set(str(T1-T2))
        Operation_Text.set('')
      elif Operation == '+' :

        T1 = float(Enter_Text.get())
        T2 = float(Other_Text.get())
        Other_Text.set('')
        Enter_Text.set(str(T1+T2))
        Operation_Text.set('')
      elif Operation == '' :

        messagebox.showerror('ERROR', 'INPUT ERROR')
    else :
      Temp_Text = Other_Text.get()
      Other_Text.set('')
      Operation_Text.set('')
      Enter_Text.set(Temp_Text)
  elif Other_Text.get() == '' and Enter_Text.get() == '':
    messagebox.showerror('ERROR', 'INPUT ERROR')

def Add_Number(number):
  Temp_Text = Enter_Text.get()
  Temp_Text = Temp_Text + str(number)
  Enter_Text.set(Temp_Text)

def Operation(Operation) :

  if Other_Text.get() != '' and  Enter_Text.get() != '':
    if Operation == '√' :
      Operation_Text.set(Operation)
      Other_Text.set('')
    else :
      Operation_Text.set(Operation)
      Answer()
      Operation_Text.set(Operation)
      Temp_Text = Enter_Text.get()
      Other_Text.set(Temp_Text)
      Enter_Text.set('')
  else :
    if Operation == '√' :
      Operation_Text.set(Operation)
    else :
      Operation_Text.set(Operation)
      Temp_Text = Enter_Text.get()
      Other_Text.set(Temp_Text)
      Enter_Text.set('')
    
def Clear() :
  Other_Text.set('')
  Operation_Text.set('')
  Enter_Text.set('')

def EXIT_BT():
  exit()

#----------------- `defs of enent of button` ---------------

def Enter_BT_0(event):
  Bt_0.config(image = Pic_0_C2)

def Leave_BT_0(event):
  Bt_0.config(image = Pic_0_C1)

def Leave_BT_1(envent):
  Bt_1.config(image = Pic_1_C1)

def Enter_BT_1(event):
  Bt_1.config(image = Pic_1_C2)

def Leave_BT_2(envent):
  Bt_2.config(image = Pic_2_C1)

def Enter_BT_2(event):
  Bt_2.config(image = Pic_2_C2)

def Leave_BT_3(envent):
  Bt_3.config(image = Pic_3_C1)

def Enter_BT_3(event):
  Bt_3.config(image = Pic_3_C2)

def Leave_BT_4(envent):
  Bt_4.config(image = Pic_4_C1)

def Enter_BT_4(event):
  Bt_4.config(image = Pic_4_C2)

def Leave_BT_5(envent):
  Bt_5.config(image = Pic_5_C1)

def Enter_BT_5(event):
  Bt_5.config(image = Pic_5_C2)

def Leave_BT_6(envent):
  Bt_6.config(image = Pic_6_C1)

def Enter_BT_6(event):
  Bt_6.config(image = Pic_6_C2)

def Leave_BT_7(envent):
  Bt_7.config(image = Pic_7_C1)

def Enter_BT_7(event):
  Bt_7.config(image = Pic_7_C2)

def Leave_BT_8(envent):
  Bt_8.config(image = Pic_8_C1)

def Enter_BT_8(event):
  Bt_8.config(image = Pic_8_C2)

def Leave_BT_9(envent):
  Bt_9.config(image = Pic_9_C1)

def Enter_BT_9(event):
  Bt_9.config(image = Pic_9_C2)

def Leave_BT_Point(envent):
  Bt_Point.config(image = Pic_Point_C1)

def Enter_BT_Point(event):
  Bt_Point.config(image = Pic_Point_C2)

def Leave_BT_Subtraction(envent):
  Bt_Subtraction.config(image = Pic_Subtraction_C1)

def Enter_BT_Subtraction(event):
  Bt_Subtraction.config(image = Pic_Subtraction_C2)

def Leave_BT_Plus(envent):
  Bt_Plus.config(image = Pic_Plus_C1)

def Enter_BT_Plus(event):
  Bt_Plus.config(image = Pic_Plus_C2)

def Leave_BT_D(envent):
  Bt_D.config(image = Pic_D_C1)

def Enter_BT_D(event):
  Bt_D.config(image = Pic_D_C2)

def Leave_BT_X(envent):
  Bt_X.config(image = Pic_X_C1)

def Enter_BT_X(event):
  Bt_X.config(image = Pic_X_C2)

def Leave_BT_Answer(envent):
  Bt_Answer.config(image = Pic_Answer_C1)

def Enter_BT_Answer(event):
  Bt_Answer.config(image = Pic_Answer_C2)

def Leave_BT_R(envent):
  Bt_R.config(image = Pic_R_C1)

def Enter_BT_R(event):
  Bt_R.config(image = Pic_R_C2)

def Leave_BT_D2(envent):
  Bt_D2.config(image = Pic_D2_C1)

def Enter_BT_D2(event):
  Bt_D2.config(image = Pic_D2_C2)

def Enter_BT_C(event):
  Bt_C.config(image = Pic_C_C2)

def Leave_BT_C(envent):
  Bt_C.config(image = Pic_C_C1)

def Enter_BT_E(event):
  Bt_E.config(image = Pic_E_C2)

def Leave_BT_E(envent):
  Bt_E.config(image = Pic_E_C1)


#----------------- `Buttons & Entrys` ---------------

Input_Text = Entry(Calcu,textvariable= Enter_Text, font = '40px')
Input_Text.grid(row = 0, column = 0, columnspan =2, rowspan=2)

Operation_T = Entry(Calcu,textvariable= Operation_Text, state = 'disabled')
Operation_T.grid(row = 0, column = 2, columnspan =2, ipadx=50)

Other_T = Entry(Calcu,textvariable= Other_Text, state = 'disabled')
Other_T.grid(row = 1, column = 2, columnspan =2, ipadx=50)

Bt_0 = Button(Calcu, image = Pic_0_C1, command = lambda : [Add_Number(0)], height=100, width=100) # Number 0
Bt_0.grid(row = 6, column = 0, sticky = W, padx = 2, pady = 2)
Bt_0.bind('<Enter>', Enter_BT_0)
Bt_0.bind('<Leave>', Leave_BT_0)

Bt_1 = Button(Calcu, image = Pic_1_C1, command = lambda : [Add_Number(1)], height=100, width=100) # Number 1
Bt_1.grid(row = 5, column = 0, sticky = N, padx = 2, pady = 2)
Bt_1.bind('<Enter>', Enter_BT_1)
Bt_1.bind('<Leave>', Leave_BT_1)

Bt_2 = Button(Calcu, image = Pic_2_C1, command = lambda : [Add_Number(2)], height=100, width=100) # Number 2
Bt_2.grid(row = 5, column = 1, sticky = N, padx = 2, pady = 2)
Bt_2.bind('<Enter>', Enter_BT_2)
Bt_2.bind('<Leave>', Leave_BT_2)

Bt_3 = Button(Calcu, image = Pic_3_C1, command = lambda : [Add_Number(3)], height=100, width=100) # Number 3
Bt_3.grid(row = 5, column = 2, sticky = N, padx = 2, pady = 2)
Bt_3.bind('<Enter>', Enter_BT_3)
Bt_3.bind('<Leave>', Leave_BT_3)

Bt_4 = Button(Calcu, image = Pic_4_C1, command = lambda : [Add_Number(4)], height=100, width=100) # Number 4
Bt_4.grid(row = 4, column = 0, sticky = N, padx = 2, pady = 2)
Bt_4.bind('<Enter>', Enter_BT_4)
Bt_4.bind('<Leave>', Leave_BT_4)

Bt_5 = Button(Calcu, image = Pic_5_C1, command = lambda : [Add_Number(5)], height=100, width=100) # Number 5
Bt_5.grid(row = 4, column = 1, sticky = N, padx = 2, pady = 2)
Bt_5.bind('<Enter>', Enter_BT_5)
Bt_5.bind('<Leave>', Leave_BT_5)

Bt_6 = Button(Calcu, image = Pic_6_C1, command = lambda : [Add_Number(6)], height=100, width=100) # Number 6
Bt_6.grid(row = 4, column = 2, sticky = N, padx = 2, pady = 2)
Bt_6.bind('<Enter>', Enter_BT_6)
Bt_6.bind('<Leave>', Leave_BT_6)

Bt_7 = Button(Calcu, image = Pic_7_C1, command = lambda : [Add_Number(7)], height=100, width=100) # Number 7
Bt_7.grid(row = 3, column = 0, sticky = N, padx = 2, pady = 2)
Bt_7.bind('<Enter>', Enter_BT_7)
Bt_7.bind('<Leave>', Leave_BT_7)

Bt_8 = Button(Calcu, image = Pic_8_C1, command = lambda : [Add_Number(8)], height=100, width=100) # Number 8
Bt_8.grid(row = 3, column = 1, sticky = N, padx = 2, pady = 2)
Bt_8.bind('<Enter>', Enter_BT_8)
Bt_8.bind('<Leave>', Leave_BT_8)

Bt_9 = Button(Calcu, image = Pic_9_C1, command = lambda : [Add_Number(9)], height=100, width=100) # Number 9
Bt_9.grid(row = 3, column = 2, sticky = N, padx = 2, pady = 2)
Bt_9.bind('<Enter>', Enter_BT_9)
Bt_9.bind('<Leave>', Leave_BT_9)

Bt_Point = Button(Calcu, image = Pic_Point_C1, command = lambda : [Add_Number('.')], height=100, width=100) # Point `.`
Bt_Point.grid(row = 6, column = 1, sticky = W, padx = 2, pady = 2)
Bt_Point.bind('<Enter>', Enter_BT_Point)
Bt_Point.bind('<Leave>', Leave_BT_Point)

Bt_Subtraction = Button(Calcu, image = Pic_Subtraction_C1, command = lambda : [Operation('-')], height=100, width=100) # Button `-`
Bt_Subtraction.grid(row = 4, column = 3, sticky = N, padx = 2, pady = 2)
Bt_Subtraction.bind('<Enter>', Enter_BT_Subtraction)
Bt_Subtraction.bind('<Leave>', Leave_BT_Subtraction)

Bt_Plus = Button(Calcu, image = Pic_Plus_C1, command = lambda : [Operation('+')], height=100, width=100) # Button `+`
Bt_Plus.grid(row = 5, column = 3, sticky = N, padx = 2, pady = 2)
Bt_Plus.bind('<Enter>', Enter_BT_Plus)
Bt_Plus.bind('<Leave>', Leave_BT_Plus)

Bt_D = Button(Calcu, image = Pic_D_C1, command = lambda : [Operation('➗')], height=100, width=100) # Button `➗`
Bt_D.grid(row = 2, column = 3, sticky = N, padx = 2, pady = 2)
Bt_D.bind('<Enter>', Enter_BT_D)
Bt_D.bind('<Leave>', Leave_BT_D)

Bt_X = Button(Calcu, image = Pic_X_C1, command = lambda : [Operation('x')], height=100, width=100) # Button `x`
Bt_X.grid(row = 3, column = 3, sticky = N, padx = 2, pady = 2)
Bt_X.bind('<Enter>', Enter_BT_X)
Bt_X.bind('<Leave>', Leave_BT_X)

Bt_Answer = Button(Calcu, image = Pic_Answer_C1, command = lambda : [Answer()], height=100, width=100) # Button `=`
Bt_Answer.grid(row = 6, column = 2, sticky = W, padx = 2, pady = 2)
Bt_Answer.bind('<Enter>', Enter_BT_Answer)
Bt_Answer.bind('<Leave>', Leave_BT_Answer)

Bt_R = Button(Calcu, image = Pic_R_C1, command = lambda : [Operation('√')], height=100, width=100) # Button `√`
Bt_R.grid(row = 2, column = 1, sticky = N, padx = 2, pady = 2)
Bt_R.bind('<Enter>', Enter_BT_R)
Bt_R.bind('<Leave>', Leave_BT_R)

Bt_D2 = Button(Calcu, image = Pic_D2_C1, command = lambda : [Operation('%')], height=100, width=100) # Button `%`
Bt_D2.grid(row = 2, column = 2, sticky = N, padx = 2, pady = 2)
Bt_D2.bind('<Enter>', Enter_BT_D2)
Bt_D2.bind('<Leave>', Leave_BT_D2)

Bt_C = Button(Calcu, image = Pic_C_C1, command = Clear, height=100, width=100) # Button `C` => clear!
Bt_C.grid(row = 2, column = 0, sticky = N, padx = 2, pady = 2)
Bt_C.bind('<Enter>', Enter_BT_C)
Bt_C.bind('<Leave>', Leave_BT_C)

Bt_E = Button(Calcu, image = Pic_E_C1, command = EXIT_BT, height=100, width=100) # Button `E` => exit!
Bt_E.grid(row = 6, column = 3, sticky = N, padx = 2, pady = 2)
Bt_E.bind('<Enter>', Enter_BT_E)
Bt_E.bind('<Leave>', Leave_BT_E)

Calcu.mainloop()
