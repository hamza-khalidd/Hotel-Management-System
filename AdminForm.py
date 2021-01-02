from tkinter import *
from tkinter import messagebox
import AdminMainMenu as amm


# ---> Admin Form Coding
def main_admin_form():
    af = Toplevel()
    af.geometry('1010x600+250+100')
    af.title('WELCOME TO | HA - HMS | ')
    af.resizable(0, 0)

    pht = PhotoImage(file="Admin_Entry _Image.png")
    label = Label(af, image=pht)
    label.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(af, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global pas_ad
    pas_ad = StringVar()
    pass_txt = Entry(af, textvar=pas_ad, show="*",bg='light grey', font=('constantia', 24, 'bold')).place(x=340, y=350)
    btn_proceed = Button(af, text=" PROCEED ",bg='light grey',relief='flat', width=20, command=admin_entry_process, font=('Bradley Hand ITC', 20, 'bold')).place(x=340, y=500)
    af.mainloop()

# ---> Admin Entry Scenerio
def admin_entry_process():
    pas_ad_info = pas_ad.get()
    global count
    for _ in range(1):
        if count == 3:
            messagebox.showwarning('Error','Exiting Application')
            exit()

        elif pas_ad_info == 'hamza' or pas_ad_info == 'anusha':
            count = 0
            amm.admin_mainmenu_form()
        else:
            messagebox.showinfo('Error','Invalid Password')
            count += 1

count = 1
