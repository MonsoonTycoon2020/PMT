from tkinter import *
#import tk


#    Label(root, text = f'{name}, SCANNED', pady=20, bg='#20b2aa').pack()

root = Tk()
root.geometry("600x400")
root.title("RFID Scanner")
#print(root.config().keys())

idName = StringVar()

def scanID():
    name = idName.get()
    print ("Input was: " + name)
    idName.set("")

root['bg'] = '#20b2aa'
frm = Frame(root, width = 100, height = 100, bg = '#20b2aa').pack()
label = Label(root, text="CodeNinjas RFID Scanner (Russian Poverty Style)", font='Arial 24 bold').place(relx=0.5, rely=0.5, anchor=CENTER)
#print(root.configure().keys())
button = Button(frm, text="Quit", command=root.destroy).pack(side=BOTTOM)
subB = Button(frm, text = "SUBMIT", command = scanID).pack(side=RIGHT)
l1= Label(frm, text="Please Scan Wristband").pack(side=TOP)
entry = Entry(root, textvariable=idName).pack(side = BOTTOM)
root.mainloop()