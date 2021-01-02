from tkinter import *
from tkinter import messagebox

class node:
    def __init__(self, data):
        self.data = data
        self.link = None

class linklist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode=node(data)
        if self.head:
            current=self.head
            while current.link:
                current=current.link
            current.link=newNode
        else:
            self.head=newNode


    def print(self):
        node=self.head
        while node!=None:
            print(node.data,end="")
            node=node.link
        print("",end=" ")

def insertionSort(head):
        if head == None:
            return None
        # Make the first node the start of the sorted list.
        sortedList = head
        head = head.link
        sortedList.link = None
        while head != None:
            current = head
            head = head.link
            if current.data < sortedList.data:
                # Advance the nodes
                current.link = sortedList
                sortedList = current
            else:
                # Search list for correct position of current.
                search = sortedList
                while search.link != None and current.data > search.link.data:
                    search = search.link
                # current goes after search.
                current.link = search.link
                search.link = current
        return sortedList

def printList(head):
    node = head
    while node != None:
        list_reg_data.insert(END,node.data)
        node = node.link

def sort_p():
    ll = linklist()
    f = open('Registered_Users' , 'r')
    ff = f.readlines()
    for i in ff:
        ll.insert(i)

    result = insertionSort(ll.head)
    printList(result)


# ---> Room Booking User Details
def admin_show_registereduser_form():
    ru = Toplevel()
    ru.geometry('1010x600+250+100')
    ru.title('WELCOME TO | HA - HMS | ')
    ru.resizable(0,0)

    pht = PhotoImage(file="Registered_Users_Data_Image.png")
    label = Label(ru, image=pht)
    label.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ru, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global list_reg_data
    list_reg_data = Listbox(ru, height=16, width=57,bg='light grey', font=('consolas', 15, 'bold'))
    list_reg_data.place(x=305, y=190)
    btn_register = Button(ru, text=" SHOW \n DATA ",bg='light grey',relief='flat', width=12,height=2, command=sort_p, font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=350)
    ru.mainloop()

