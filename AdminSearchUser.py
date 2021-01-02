from tkinter import *
from tkinter import messagebox

def search_s():
    srch = search_name.get()
    list_sr_data.delete('0', 'end')
    with open('Registered_Users') as reg_users:
        for users in reg_users:
            if users.split(',')[0] == srch:
                list_sr_data.insert(END,users)

def delete_s():
    serch = search_name.get()
    with open("Registered_Users", "r") as f:
        lines = f.readlines()
    with open("Registered_Users", "w") as f:
        for line in lines:
            if line.split(',')[0] != serch:
                f.write(line)

    list_sr_data.delete('0', 'end')


# ---> Room Booking User Details
def admin_search_reguser_form():
    ru = Toplevel()
    ru.geometry('1010x600+250+100')
    ru.title('WELCOME TO | HA - HMS | ')
    ru.resizable(0,0)

    pht = PhotoImage(file='Search_Register_User_Image.png')
    lbl = Label(ru, image=pht)
    lbl.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ru, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global list_sr_data
    list_sr_data = Listbox(ru, height=12, width=57,bg='light grey', font=('consolas', 15, 'bold'))
    list_sr_data.place(x=305, y=250)
    global search_name
    search_name = StringVar()
    global searchtxt
    searchtxt = Entry(ru,textvar=search_name,bg='light grey', font=('constantia', 20, 'bold')).place(x=540,y=180)
    btn_register = Button(ru, text=" SEARCH \n USER ",bg='light grey',relief='flat', width=13,height=2, command=search_s, font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=260)
    btn_register = Button(ru, text=" DELETE \n USER ",bg='light grey',relief='flat', width=13, height=2, command=delete_s,font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=410)

    ru.mainloop()
