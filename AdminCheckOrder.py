from tkinter import *
from tkinter import messagebox

# ---> FIFO Way Order Details
def admin_show_firstorder_form():
    fou = Toplevel()
    fou.geometry('1010x600+250+100')
    fou.title('WELCOME TO | HA - HMS | ')
    fou.resizable(0,0)

    pht = PhotoImage(file="Check_Food_Order_Image.png")
    label = Label(fou, image=pht)
    label.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(fou, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global list_ordercheck_data
    list_ordercheck_data = Listbox(fou, height=10, width=57,bg='light grey', font=('consolas', 15, 'bold'))
    list_ordercheck_data.place(x=290, y=285)
    btn_register = Button(fou, text=" SHOW LINE \n BY  \n LINE ORDER ",bg='light grey',relief='flat', width=12,height=3, command=linebylineorder_code, font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=350)
    fou.mainloop()


def linebylineorder_code():
    list_ordercheck_data.delete('0', 'end')
    i = st.pop()
    list_ordercheck_data.insert(END, i)

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        file = open('BookedTable_Users', 'r')
        f = file.readlines()
        for num in f:
            st.push(num)
        return self.queue.pop(0)


st = Queue()
# -----------------------------------------------------------------