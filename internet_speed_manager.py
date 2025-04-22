from tkinter import *
import speedtest 

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_up.configure(text=up)
    lab_down.config(text=down)


sp = Tk()
sp.title("Internet Speed  Test")
sp.geometry("500x700")
sp.config(bg="blue")

#lab = Label(sp, text = "Internet Speed Test ",font =("Time New Roman",20,"bold" ,bg="Blue",fg="white"))
lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 20, "bold"), bg= "#1e1e2e" , fg="white")
lab.place(x=60,y=40,height=50,width=380)



lab = Label(sp,text = "Download  Speed ",font = ("Time New Roman",20,"bold"),bg="#2a2a3a")
lab.place(x=55,y=130,height=50,width=380)

lab_down = Label(sp,text = " 00 ",font = ("Time New Roman",20,"bold"))
lab_down.place(x=55,y=200,height=50,width=380)

lab = Label(sp,text = "Upload Speed ",font = ("Time New Roman",20,"bold"),bg="#2a2a3a")
lab.place(x=55,y=290 ,height=50,width=380)

lab_up = Label(sp,text = "00",font = ("Time New Roman",20,"bold"))
lab_up.place(x=55,y=360,height=50,width=380)

button = Button(sp,text = "Check Speed", font = ("Time New Roman ",30 ,"bold"),relief=RAISED , bg="Red",command=speedcheck)
button.place(x=125, y=450, height=50, width=250)
sp.mainloop()
