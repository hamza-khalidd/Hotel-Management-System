from tkinter import *
from tkinter import messagebox
import SignupForm as s
import AdminForm as a
import LoginForm as l
import LocationFinder as lf

# ---> Main Opening Form Of HOTEL MANAGEMENT SYSTEM
def opening_form():
    global mf
    mf = Tk()
    mf.geometry('1010x600+250+100')
    mf.title('WELCOME TO | HA - HMS | ')
    mf.resizable(0, 0)
    photo = PhotoImage(file="MainFormImage.png")
    label = Label(mf,image=photo)
    label.pack()

    btn_nextform = Button(mf, text="HOTEL MANAGEMENT SYSTEM",bg='light grey',relief='flat', width=50, font=('Bradley Hand ITC', 24, 'bold'),command=main_selection_form).place(x=28, y=520)
    mf.mainloop()

# ---> Main Selection Form Where You Can Select Path To Login,Admin OR Signup
def main_selection_form():
    mf.withdraw()
    global ef
    ef = Toplevel()
    ef.geometry('1010x600+250+100')
    ef.title('WELCOME TO | HA - HMS | ')
    ef.resizable(0, 0)

    pht = PhotoImage(file="Main_Selection_Image.png")
    label = Label(ef, image=pht)
    label.pack()

    photo_su = PhotoImage(file="Btn_MainSelection_SignUp_Image.png")
    photo_a = PhotoImage(file="Btn_MainSelection_Admin_Image.png")
    photo_l = PhotoImage(file="Btn_MainSelection_Login_Image.png")
    photo_lo = PhotoImage(file="btn_lf_image.png")
    photo_e = PhotoImage(file="btn_exit_image.png")

    btn_login = Button(ef, width=190, height=180,relief='flat', image=photo_l, command=l.main_login_form)
    btn_login.place(x=100, y=260)
    btn_admin = Button(ef, width=190, height=180,relief='flat', image=photo_a, command=a.main_admin_form)
    btn_admin.place(x=400, y=260)
    btn_signup = Button(ef, width=190, height=180,relief='flat', image=photo_su, command=s.main_signup_form)
    btn_signup.place(x=700, y=260)
    btn_team = Button(ef, width=74, height=74, relief='flat', image=photo_lo, command=lf.LocationFinderGUI)
    btn_team.place(x=920, y=510)
    btn_exit = Button(ef, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    mainloop()

# ---> Main Method Code
opening_form()