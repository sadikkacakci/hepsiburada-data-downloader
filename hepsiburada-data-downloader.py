from tkinter import *
from tkinter import messagebox
from hepsiburada import HepsiBurada,processing
root = Tk()

root.title("Hepsiburada Data Downloader")
root.geometry('300x200')
root.configure(background="white")
root.resizable(False,False) 

def clearEntry():
    entry1.delete(0,"end")

def activeClass(word):
    hpsiburada = HepsiBurada(processing(word))
    return hpsiburada

def activeGetPrices(word):
    hpsiburada = activeClass(word)
    hpsiburada.getPrices()

def activeWriteExcel(word):
    hpsiburada = activeClass(word)
    try:
        hpsiburada.writeExcel()
    except:
        messagebox.showinfo("Hata!","İndirme işlemi başarısız.")
    messagebox.showinfo("Başarılı",'İndirme işlemi başarıyla gerçekleşti.')

def activeWriteCsv(word):
    hpsiburada = activeClass(word)
    try:
        hpsiburada.writeCsv()
    except:
        messagebox.showinfo("Hata!","İndirme işlemi başarısız.")
    messagebox.showinfo("Başarılı",'İndirme işlemi başarıyla gerçekleşti.')

def activeWriteTxt(word):
    hpsiburada = activeClass(word)
    try:
        hpsiburada.writeTxt()
    except:
        messagebox.showinfo("Hata!","İndirme işlemi başarısız.")
        return
    messagebox.showinfo("Başarılı",'İndirme işlemi başarıyla gerçekleşti.')

entry1 = Entry(root,width = 50,fg ="black",bg = "white",borderwidth=2,font = ("Arial",10))
entry1.pack(padx=30, pady=40)
entry1.insert(0,"Enter the name of the product...")
entry1.bind("<FocusIn>", lambda event:clearEntry())


# search_button = Button(root,text= "Search",height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10), command = lambda:activeGetPrices(entry1.get()))
# search_button.place(relx=0.5, rely=0.5, anchor=CENTER)

excel_button = Button(root,text= "Excel",height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10),command = lambda: activeWriteExcel(entry1.get()))
excel_button.place(relx=0.2, rely=0.6, anchor=CENTER)

csv_button = Button(root,text= "Csv",height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10),command = lambda: activeWriteCsv(entry1.get()))
csv_button.place(relx=0.5, rely=0.6, anchor=CENTER)

txt_button = Button(root,text= "Txt",height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10),command = lambda: activeWriteTxt(entry1.get()))
txt_button.place(relx=0.8, rely=0.6, anchor=CENTER)

root.mainloop()