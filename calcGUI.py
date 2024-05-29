import tkinter as tk

mainsc=tk.Tk()
mainsc.geometry("300x400")

label = tk.Label(mainsc,text = "Calculator")
label.config(font=("Coureir",18,"bold"))
label.place (x = 90, y = 10)

entry=tk.Entry(mainsc,bd=6,width=40)
entry.place(x = 20, y = 45)

btn=tk.Button(mainsc,text="+",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=20,y=80)

btn=tk.Button(mainsc,text="CE",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=105,y=80)

btn=tk.Button(mainsc,text="=",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=190,y=80)

btn=tk.Button(mainsc,text="-",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=20,y=130)

btn=tk.Button(mainsc,text="*",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=105,y=130)

btn=tk.Button(mainsc,text="/",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=190,y=130)

btn=tk.Button(mainsc,text="1",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=20,y=180)

btn=tk.Button(mainsc,text="2",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=105,y=180)

btn=tk.Button(mainsc,text="3",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=190,y=180)

btn=tk.Button(mainsc,text="4",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=20,y=230)

btn=tk.Button(mainsc,text="5",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=105,y=230)

btn=tk.Button(mainsc,text="6",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=190,y=230)

btn=tk.Button(mainsc,text="7",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=20,y=280)

btn=tk.Button(mainsc,text="8",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=105,y=280)

btn=tk.Button(mainsc,text="9",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=190,y=280)

btn=tk.Button(mainsc,text=".",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=20,y=330)

btn=tk.Button(mainsc,text="0",width=10,height=2,background="lightgreen",activebackground="lightblue",bd=5,font=("Coureir",7,"bold"))
btn.place(x=105,y=330)

btn=tk.Button(mainsc,text="+/-",width=10,height=2,background="lightblue",activebackground="lightgreen",bd=5,font=("Coureir",7,"bold"))
btn.place(x=190,y=330)

mainsc.mainloop()
