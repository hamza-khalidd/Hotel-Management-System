from tkinter import *
import os
from tkinter import messagebox
import LoginForm as lf
import webbrowser
import User_Bookings as ub


# ---> User MainMenu
def user_mainmenu_form():
    ummf = Toplevel()
    ummf.geometry('1010x600+250+100')
    ummf.title('WELCOME TO | HA - HMS | ' + lf.name_info)
    ummf.resizable(0, 0)

    pht = PhotoImage(file='User_MainMenu_Image.png')
    lbl = Label(ummf, image=pht)
    lbl.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ummf, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)


    photo_room = PhotoImage(file="MainMenu_Room.png")
    photo_table = PhotoImage(file="MainMenu_Order.png")
    photo_extra = PhotoImage(file="Main_Menu_Extra.png")
    photo_fea = PhotoImage(file="Main_Menu_AboutUs.png")
    photo_con = PhotoImage(file="Main_Menu_Contact.png")
    photo_rec = PhotoImage(file="MainMenu_Receipt.png")
    btn_room = Button(ummf, width=180, height=170,relief='flat', image=photo_room, command=ub.user_room_booking).place(x=280, y=170)
    btn_table = Button(ummf, width=180, height=170,relief='flat', image=photo_table, command=ub.user_table_booking).place(x=530, y=170)
    btn_extra = Button(ummf, width=180, height=170,relief='flat', image=photo_extra, command=user_extras).place(x=780, y=170)
    btn_fea = Button(ummf, width=180, height=170,relief='flat', image=photo_fea, command=snd1).place(x=260, y=380)
    btn_con = Button(ummf, width=180, height=170,relief='flat', image=photo_con, command=user_contact_us).place(x=510, y=380)
    btn_rec = Button(ummf, width=180, height=170, relief='flat', image=photo_rec, command=ub.user_receipt).place(x=760,y=380)
    mainloop()

# ---> Function Respondible To Play Video When Called ...
def snd1():
    os.system("videohotel.mp4")

# ---> Function Responsible To Show Contact Us Form And Info When Called
def user_contact_us():
    ucu = Toplevel()
    ucu.geometry('1010x600+250+100')
    ucu.title('Contact Us')
    ucu.resizable(0, 0)

    pht = PhotoImage(file='ContactUs_Image.png')
    lbl = Label(ucu, image=pht)

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ucu, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    btn_register = Button(ucu, text=" OPEN \n WEBSITE ",bg='light grey',relief='flat', width=12, height=2, command=openw,font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=350)

    lbl.pack()

    ucu.mainloop()

# ---> Function Responsible To Show Contact Us Form And Info When Called
def user_extras():
    ucu = Toplevel()
    ucu.geometry('1010x600+250+100')
    ucu.title('Contact Us')
    ucu.resizable(0, 0)

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ucu, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    pht = PhotoImage(file='Extras_Image.png')
    lbl = Label(ucu, image=pht)
    lbl.pack()

    ucu.mainloop()

# ---> Contact Us : Two Sub Functions For Opening Web Browser
def openw():
    webbrowser.open("http://www.hotelmehran.com/")

# ---> Main Method Calling