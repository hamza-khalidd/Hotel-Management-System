from tkinter import *
from tkinter import ttk

def treecode():
    app = Toplevel()
    app.geometry('1010x600+250+100')
    app.resizable(0,0)

    phtttt = PhotoImage(file='Hotel_Team_Image.png')
    lbl = Label(app, image=phtttt)
    lbl.place(x=0,y=0)

    app.title("WELCOME TO | HA - HMS | ")
    treeview = ttk.Treeview(app,height=11)
    treeview.pack(fill=X,expand=True)
    treeview.insert('', '0', 'item1', text='HA - HMS')
    treeview.insert('', '1', 'item2', text='Hamza Khalid (The One Who Dreams To Start This)')
    treeview.insert('', '2', 'item3', text='Anusha Iqbal (The One Who Believes In His Friends Dream)')
    treeview.insert('item2', 'end', 'A', text='T-Management')
    treeview.insert('item2', 'end', 'B', text='T-Parking')
    treeview.insert('item2', 'end', 'C', text='T-Logistics')
    treeview.insert('item3', 'end', 'D', text='T-Hospitality')
    treeview.insert('item3', 'end', 'E', text='T-Sales')
    treeview.insert('item3', 'end', 'F', text='T-Maintenance')
    treeview.move('item2', 'item1', 'end')
    treeview.move('item3', 'item1', 'end')
    app.mainloop()