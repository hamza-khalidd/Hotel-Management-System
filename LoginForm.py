from tkinter import *
from tkinter import messagebox
import UserMainMenu as umm

# ---> Login Form Coding
def main_login_form():
    af = Toplevel()
    af.geometry('1010x600+250+100')
    af.title('WELCOME TO | HA - HMS | ')
    af.resizable(0, 0)



    phtt = PhotoImage(file='User_Entry_Image.png')
    lbl = Label(af, image=phtt)
    lbl.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(af, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global id_us
    id_us = StringVar()
    pass_txt = Entry(af, textvar=id_us,bg='light grey', font=('constantia', 20, 'bold')).place(x=450, y=300)
    global pas_us
    pas_us = StringVar()
    pass_txt = Entry(af, textvar=pas_us, show="*",bg='light grey', font=('constantia', 20, 'bold')).place(x=445, y=393)
    global lblmsg
    btn_login = Button(af, text=" LOG IN ",bg='light grey',relief='flat', width=20, command=login_check, font=('Bradley Hand ITC', 20, 'bold')).place(x=350, y=510)
    af.mainloop()

def login_check():
    global name_info
    name_info = id_us.get()
    pass_info = pas_us.get()

    with open('Registered_Users') as reg_users:
        for users in reg_users:
            if users.split(',')[0] == name_info:
                if users.split(',')[1] == pass_info:
                    umm.user_mainmenu_form()