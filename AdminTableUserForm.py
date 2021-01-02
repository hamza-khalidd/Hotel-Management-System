from tkinter import *
from tkinter import messagebox

def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp


   return rightmark


def sort_p():
    alist = []
    ff = open('BookedTable_Users', 'r')
    f = ff.readlines()
    for i in f:
        alist.append(i)

    n = len(alist)

    quickSort(alist)

    for i in range(0,len(alist)):
        list_table_data.insert(END, alist[i])


# ---> Room Booking User Details
def admin_show_tableuser_form():
    ru = Toplevel()
    ru.geometry('1010x600+250+100')
    ru.title('WELCOME TO | HA - HMS | ')
    ru.resizable(0,0)

    pht = PhotoImage(file='Table_Bookings_Data_Image.png')
    lbl = Label(ru, image=pht)
    lbl.pack()

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ru, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    global list_table_data
    list_table_data = Listbox(ru, height=16, width=57,bg='light grey', font=('consolas', 15, 'bold'))
    list_table_data.place(x=310, y=190)
    btn_register = Button(ru, text=" SHOW TABLE \n DATA ",bg='light grey',relief='flat', width=12,height=2, command=sort_p, font=('Bradley Hand ITC', 20, 'bold')).place(x=40, y=350)
    ru.mainloop()

