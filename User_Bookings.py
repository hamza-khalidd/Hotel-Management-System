from tkinter import *
from tkinter import messagebox
import UserMainMenu as umm
# -----------------------------------------------

# ---> IMPLEMENTATION OF STACK
class Stack():
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()

    def peep(self):
        n=len(self.stack)
        return self.stack[n-1]

    def display(self):
        return self.stack


st = Stack()


# ---> Function Responsible To Show Room Booking Form GUI When Called
def user_room_booking():
    urb = Toplevel()
    urb.geometry('1010x600+250+100')
    urb.title('WELCOME TO | HA - HMS | ')
    urb.resizable(0,0)

    pht = PhotoImage(file='Room_Bookings_Image.png')
    lbl = Label(urb, image=pht)
    lbl.pack()

    global name
    name = StringVar()
    name_txt = Entry(urb, textvar=name,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=230, y=270)
    global rtype
    rtype = StringVar()
    pass_txt = Entry(urb, textvar=rtype ,bg='lightgrey',font=('constantia', 16, 'bold')).place(x=730, y=265)
    global cont
    cont = StringVar()
    num_txt = Entry(urb, textvar=cont,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=250, y=355)
    global rel
    rel = StringVar()
    rel_txt = Entry(urb, textvar=rel,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=725, y=355)
    global cnic
    cnic = StringVar()
    cnic_txt = Entry(urb, textvar=cnic,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=220, y=440)
    global num_people
    num_people = StringVar()
    gen_txt = Entry(urb, textvar=num_people,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=740, y=440)
    btn_register = Button(urb, text=" BOOK ROOM NOW ",bg='light grey',relief='flat', width=20, command=register_into_textfile_room, font=('Bradley Hand ITC', 20, 'bold')).place(x=350, y=510)
    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(urb, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)
    urb.mainloop()

# ---> Room Booking Code
def register_into_textfile_room():
    name_info = name.get()
    rtype_info = rtype.get()
    cont_info = cont.get()
    rel_info = rel.get()
    cnic_info = cnic.get()
    num_people_info = num_people.get()

    ll = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    f = open('BookedRooms_Users', 'r')
    ff = f.readlines()
    n = len(ff)

    for i in range(1, n + 1):
        del ll[len(ll) - 1]

    for j in ll:
        st.push(j)
    r = st.pop()

    global bill
    if rtype_info == 'S' or rtype_info == 's':
        bill = 1000 * int(num_people_info)

    elif rtype_info == 'L' or rtype_info == 'l':
        bill = 2000 * int(num_people_info)

    fil = open('BookedRooms_Users','a')
    fil.writelines(name_info + ',' + str(r) + ',' + rtype_info + ',' + cont_info + ',' + rel_info + ',' + cnic_info + ',' + num_people_info + ',' + str(bill) + '\n')
    fil.close()
    umm.user_mainmenu_form()


# ------------------------------------------------------------------
# ---> Function Responsible To Show Table Booking Form GUI When Called
def user_table_booking():
    utb = Toplevel()
    utb.geometry('1010x600+250+100')
    utb.title('WELCOME TO | HA - HMS | ')
    utb.resizable(0,0)

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(utb, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    pht = PhotoImage(file='Table_Bookings_Image.png')
    lbl = Label(utb, image=pht)
    lbl.pack()

    global namet
    namet = StringVar()
    name_txt = Entry(utb, textvar=namet,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=230, y=270)
    global foodtype
    foodtype = StringVar()
    pass_txt = Entry(utb, textvar=foodtype,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=720, y=263)
    global contt
    contt = StringVar()
    num_txt = Entry(utb, textvar=contt,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=250, y=355)
    global ttype
    ttype = StringVar()
    rel_txt = Entry(utb, textvar=ttype,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=715, y=360)
    global cnict
    cnict = StringVar()
    cnic_txt = Entry(utb, textvar=cnict,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=215, y=440)
    global num_peoplet
    num_peoplet = StringVar()
    gen_txt = Entry(utb, textvar=num_peoplet,bg='lightgrey', font=('constantia', 16, 'bold')).place(x=735, y=440)
    btn_register = Button(utb, text=" BOOK TABLE NOW ",bg='light grey',relief='flat', width=20, command=register_into_textfile_table, font=('Bradley Hand ITC', 20, 'bold')).place(x=350, y=510)
    utb.mainloop()

# ---> Table Booking Code
def register_into_textfile_table():
    name_info = namet.get()
    foodtype_info = foodtype.get()
    cont_info = contt.get()
    ttype_info = ttype.get()
    cnic_info = cnict.get()
    num_people_info = num_peoplet.get()

    pay = 0
    if foodtype_info.lower() == 'desi':
        pay = 500

    elif foodtype_info.lower() == 'chinese':
        pay = 1000

    elif foodtype_info.lower() == 'italian':
        pay = 1500

    elif foodtype_info.lower() == 'continental':
        pay = 2000

    tpay = 0
    if ttype_info.lower() == 'simple':
        tpay = 1000

    elif ttype_info.lower() == 'vip':
        tpay = 1500

    elif ttype_info.lower() == 'sofa':
        tpay = 2000

    global bill
    n = int(num_people_info)
    bil = (n * pay) + tpay

    fil = open('BookedTable_Users','a')
    fil.writelines(name_info + ',' + foodtype_info + ',' + cont_info + ',' + ttype_info + ',' + cnic_info + ',' + num_people_info + ',' + str(bil) + '\n')
    fil.close()
    umm.user_mainmenu_form()

# ---------------------------------------------------------------------------
# ---> Receipt Form <---
def user_receipt():
    ur = Toplevel()
    ur.geometry('1010x600+250+100')
    ur.title('WELCOME TO | HA - HMS | ')
    ur.resizable(0,0)

    pht = PhotoImage(file='Main_Receipt_Image.png')
    lbl = Label(ur, image=pht)
    lbl.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ur, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global list_r_data
    list_r_data = Listbox(ur, height=15, width=57, bg='light grey', font=('consolas', 15, 'bold'))
    list_r_data.place(x=305, y=200)
    btn_register = Button(ur, text=" ROOM \n RECEIPT ", bg='light grey', relief='flat', width=13, height=2,command=room_receipt, font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=260)
    btn_register = Button(ur, text=" TABLE \n RECEIPT ", bg='light grey', relief='flat', width=13, height=2, command=table_receipt,font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=410)

    ur.mainloop()

 # ---> Room Receipt Code <---
def room_receipt():
    namee = name.get()
    list_r_data.delete('0', 'end')
    with open('BookedRooms_Users') as reg_users:
        for users in reg_users:
            if users.split(',')[0] == namee:
                list_r_data.insert(END,'-------------------------------------------')
                list_r_data.insert(END, '           ROOM BOOKING RECEIPT       ')
                list_r_data.insert(END, '-------------------------------------------')
                list_r_data.insert(END,'NAME : ' + users.split(',')[0])
                list_r_data.insert(END, 'ROOM NO : ' + users.split(',')[1])
                list_r_data.insert(END,'ROOM TYPE : ' + users.split(',')[2])
                list_r_data.insert(END,'CONTACT : ' + users.split(',')[3])
                list_r_data.insert(END,'RELIGION : ' + users.split(',')[4])
                list_r_data.insert(END,'CNIC : ' + users.split(',')[5])
                list_r_data.insert(END,'NUMBER OF PEOPLE : ' + users.split(',')[6])
                list_r_data.insert(END,'TOTAL BILL : ' + users.split(',')[7])
                list_r_data.insert(END, '\n')
                list_r_data.insert(END, '\n')
                list_r_data.insert(END, '         Pay Your Bill Within 3 Days     ')
                list_r_data.insert(END, '     Otherwise Your Booking Will be cancelled')


# ---> Table Receipt <---
 # ---> Room Receipt Code <---
def table_receipt():
    nameet = namet.get()

    list_r_data.delete('0', 'end')
    with open('BookedTable_Users') as reg_users:
        for users in reg_users:
            if users.split(',')[0] == nameet:
                list_r_data.insert(END,'-------------------------------------------')
                list_r_data.insert(END, '           TABLE BOOKING RECEIPT       ')
                list_r_data.insert(END, '-------------------------------------------')
                list_r_data.insert(END,'NAME : ' + users.split(',')[0])
                list_r_data.insert(END,'FOOD TYPE : ' + users.split(',')[1])
                list_r_data.insert(END,'CONTACT : ' + users.split(',')[2])
                list_r_data.insert(END,'TABLE TYPE : ' + users.split(',')[3])
                list_r_data.insert(END,'CNIC : ' + users.split(',')[4])
                list_r_data.insert(END,'NUMBER OF PEOPLE : ' + users.split(',')[5])
                list_r_data.insert(END,'TOTAL BILL : ' + users.split(',')[6])
                list_r_data.insert(END, '\n')
                list_r_data.insert(END, '\n')
                list_r_data.insert(END, '         Pay Your Bill Within 3 Days     ')
                list_r_data.insert(END, '     Otherwise Your Booking Will be cancelled')
