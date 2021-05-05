# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:14:51 2021

@author: Dell
"""

from tkinter import *
root = Tk()
root.title("Driving License")
root.geometry("400x250")
root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")
label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_idtag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="id:")
label_nametag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="name:")
label_dobtag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="dob:")
label_pintag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="pin no:")
label_addresstag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="address:")
label_authorisationtag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the vehicles:")

label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_authorisation = Label(root)

def button_licence():
    id_value = 19827198349
    print(type(id_value))
    name = "Yuvraj Gupta"
    print(type(name)) 
    dob = "27 August 2009"
    print(type(dob))
    pin = 3456456
    print(type(pin))
    address = "Rishikesh"
    print(type(address))
    authorisation= ["Two","Four"]
    print(type(authorisation))
    
    label_id['text'] = id_value
    label_name['text'] = name
    label_dob['text'] = dob
    label_pin['text'] = pin
    label_address['text'] = address
    label_authorisation['text'] = authorisation
    
    
button1 = Button(root, text = "Show my Driving License", command=button_licence)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_authorisation_window = canvas.create_window(335, 180, anchor=CENTER, window=label_authorisation)
canvas.pack()

root.mainloop()