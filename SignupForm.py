from tkinter import *
from tkinter import messagebox
import LoginForm as lf


# ---> People Will Fill Up Details And Will Register Here
def main_signup_form():
    suf = Toplevel()
    suf.geometry('1010x600+250+100')
    suf.title('WELCOME TO | HA - HMS | ')
    suf.resizable(0,0)

    phtt = PhotoImage(file='SignUp_Image.png')
    lbl = Label(suf, image=phtt)
    lbl.pack()

    global name
    name = StringVar()
    name_txt = Entry(suf, textvar=name,bg='light grey', font=('constantia', 16, 'bold')).place(x=270, y=270)
    global passw
    passw = StringVar()
    pass_txt = Entry(suf, textvar=passw,bg='light grey', show="*" ,font=('constantia', 16, 'bold')).place(x=730, y=265)
    global cont
    cont = StringVar()
    num_txt = Entry(suf, textvar=cont,bg='light grey', font=('constantia', 16, 'bold')).place(x=270, y=355)
    global rel
    rel = StringVar()
    rel_txt = Entry(suf, textvar=rel,bg='light grey', font=('constantia', 16, 'bold')).place(x=730, y=355)
    global cnic
    cnic = StringVar()
    cnic_txt = Entry(suf, textvar=cnic,bg='light grey', font=('constantia', 16, 'bold')).place(x=270, y=440)
    global gen
    gen = StringVar()
    gen_txt = Entry(suf, textvar=gen,bg='light grey', font=('constantia', 16, 'bold')).place(x=730, y=440)
    btn_register = Button(suf, text=" REGISTER NOW ",bg='light grey',relief='flat', width=20, command=register_into_textfile, font=('Bradley Hand ITC', 20, 'bold')).place(x=350, y=510)
    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(suf, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)
    suf.mainloop()

def register_into_textfile():
    name_info = name.get()
    passw_info = passw.get()
    cont_info = cont.get()
    rel_info = rel.get()
    cnic_info = cnic.get()
    gen_info = gen.get()

    file = open('Registered_Users', 'a')
    file.writelines(name_info + ',' + passw_info + ',' + cont_info + ',' + rel_info + ',' + cnic_info + ',' + gen_info + '\n')
    file.close()
    messagebox.showinfo('Congratulations', 'Data Entered Successfully')
    lf.main_login_form()



