from tkinter import *
from tkinter import messagebox
import AdminCheckOrder as aco
import AdminRoomUserForm as aruf
import AdminTableUserForm as atuf
import AdminRegisteredUserForm as areguf
import AdminSearchUser as asu

def admin_mainmenu_form():
    ammf = Toplevel()
    ammf.geometry('1010x600+250+100')
    ammf.title('WELCOME TO | HA - HMS | ')
    ammf.resizable(0, 0)

    pht = PhotoImage(file="Admin_MainMenu_Image.png")
    label = Label(ammf, image=pht)
    label.pack()

    photo_room = PhotoImage(file="MainMenu_Room.png")
    photo_table = PhotoImage(file="MainMenu_Order.png")
    photo_extra = PhotoImage(file="MainMenu_Registrations.png")
    photo_fea = PhotoImage(file="MainMenu_Search_User.png")
    photo_ab = PhotoImage(file="MainMenu_Table.png")
    btn_room = Button(ammf, width=180, height=170,relief='flat', image=photo_room, command=aruf.admin_show_roomuser_form).place(x=280, y=170)
    btn_table = Button(ammf, width=180, height=170,relief='flat', image=photo_table, command=atuf.admin_show_tableuser_form).place(x=530, y=170)
    btn_reg = Button(ammf, width=180, height=170, image=photo_extra,relief='flat', command=areguf.admin_show_registereduser_form).place(x=780, y=170)
    btn_fea = Button(ammf, width=180, height=170, image=photo_fea,relief='flat', command=asu.admin_search_reguser_form).place(x=410, y=380)
    btn_ab = Button(ammf, width=180, height=170, image=photo_ab,relief='flat', command=aco.admin_show_firstorder_form).place(x=650, y=380)
    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ammf, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)
    mainloop()



