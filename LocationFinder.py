from tkinter import *
from tkinter import ttk

def LocationFinderGUI():
    ucu = Toplevel()
    ucu.geometry('1010x600+250+100')
    ucu.title('Welcome To | HA - HMS |')
    ucu.resizable(0, 0)

    pht = PhotoImage(file='LocationFinderImage.png')
    lbl = Label(ucu, image=pht)
    lbl.pack()

    global ele
    ele = StringVar()
    numberChosen = ttk.Combobox(ucu,width=14,textvariable=ele,font=('constantia',20))
    numberChosen['values'] = ('Karimabad', 'Waterpump', 'Numaish', 'Gulshan', 'Defence', 'Clifton', 'KDA')
    numberChosen.place(x=484,y=266)

    photo_e = PhotoImage(file="btn_exit_image.png")
    btn_exit = Button(ucu, width=64, height=64, relief='flat', image=photo_e, command=quit)
    btn_exit.place(x=-2, y=530)

    btn_register = Button(ucu, text=" SEARCH PATH ", bg='light grey', relief='flat', width=15,command=code, font=('Bradley Hand ITC', 20, 'bold')).place(x=370, y=330)

    global list_lf_data
    list_lf_data = Listbox(ucu, height=4, width=70, bg='light grey', font=('constantia', 16, 'bold'))
    list_lf_data.place(x=78, y=430)

    ucu.mainloop()


def code():
    dt = ele.get()
    graph = {
        'HMS': set(['Karimabad', 'Gulshan','Waterpump']),
        'Karimabad': set(['HMS', 'Defence']),
        'Gulshan': set(['Karimabad', 'KDA']),
        'Defence': set(['Karimabad']),
        'Clifton': set(['Gulshan', 'KDA']),
        'KDA': set(['Gulshan', 'KDA']),
        'Waterpump': set(['Clifton', 'Defence']),
        'Numaish': set(['Gulshan', 'Karimabad','KDA'])
    }

    list_lf_data.delete('0', 'end')
    list_lf_data.insert(END,' | { } --- Indicates The Path |')
    list_lf_data.insert(END, ' ')
    list_lf_data.insert(END,list(bfs_path_finding(graph, dt, 'HMS')))

def bfs_path_finding(graph, source, destination):
    queue = [(source, [source])]
    while queue:
        vertex, path = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == destination:
                yield path + [next]  # to add multiple values
            else:
                queue.append((next, path + [next]))

#--------------------