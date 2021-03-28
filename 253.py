from tkinter import*
root = Tk()

def r(root):
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=int(e4.get())
    s=0
    while not(a==c) or not(b==d):
        if b==30:
            s=s+1

        b=b+1

        if b==60:
            a=a+1
            b=0
            if a>12:
                s=s+a-12
            else:
                s=s+a
            if a==24:
                a=0
    l5['text']=s
    

fu1=Frame(root)
fd1=Frame(root)
fu2=Frame(root)
fd2=Frame(root)
fd3=Frame(root)


l1=Label(fu1, text = "ЧАСЫ")
l2=Label(fu1, text = "МИНУТЫ")
l3=Label(fd1, text = "ЧАСЫ")
l4=Label(fd1, text = "МИНУТЫ")
l5=Label(fd3, text = "f")

e1=Entry(fu2)
e2=Entry(fu2)
e3=Entry(fd2)
e4=Entry(fd2)

b=Button(fd3, text="Решить")
b.bind('<Button-1>', r)

fu1.pack()
fu2.pack()
fd1.pack()
fd2.pack()
fd3.pack()

l1.pack(side = 'left')
l2.pack(side = 'left')
l3.pack(side = 'left')
l4.pack(side = 'left')
e1.pack(side = 'left')
e2.pack(side = 'left')
e3.pack(side = 'left')
e4.pack(side = 'left')
b.pack(side = 'left')
l5.pack(side = 'left')

root.mainloop()
