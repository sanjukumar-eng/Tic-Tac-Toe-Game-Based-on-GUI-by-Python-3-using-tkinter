#Tic Tac Toe Game Python Program Based on GUI using Tkinter.

#Importing Libraries
from tkinter import *
from tkinter import messagebox

#Forming a Class of TTT(Tic Tac Toe)
class TTT:

    #Constructor Function who load GUI
    def __init__(self):

        self.load_window()
        

    #Making GUI Function
    def load_window(self):

        #bclick object is use for change the sign ("X"->"O", "O"->"X")
        self._bclick=True
        #flag object is use for Counting Number of Clicks to Button(Simply For Traversing)
        self._flag=0
        
        self._root=Tk()
        
        self._root.title("Tic Tac Toe")
        self._root.minsize(400,700)
        self._root.maxsize(400,700)
        self._root.config(background="#F60A40")

        self.frames()
        
        self._root.mainloop()
        

    #Making Frame of GUI Function
    def frames(self):

        self._label1=Label(self._root, text="Tic Tac Toe", fg="#fff", bg="#F60A40")
        self._label1.config(font=("Arial",30))
        self._label1.pack(pady=(15,15))

        frame1=Frame(self._root)
        frame1.config(bg="#F60A40")
        frame1.pack()

        self._player1=Label(frame1, text="Player X Name:", fg="#fff", bg="#F60A40")
        self._player1.config(font=("Times",16))
        self._player1.pack(side=LEFT, pady=(5,5))

        self._player1input=Entry(frame1)
        self._player1input.pack(side=LEFT, pady=(5,5), ipady=5,ipadx=20)

        frame2=Frame(self._root)
        frame2.config(bg="#F60A40")
        frame2.pack()
        
        self._player2=Label(frame2, text="Player O Name:", fg="#fff", bg="#F60A40")
        self._player2.config(font=("Times",16))
        self._player2.pack(side=LEFT, pady=(5,5))

        self._player2input=Entry(frame2)
        self._player2input.pack(side=LEFT, pady=(5,5), ipady=5,ipadx=20)

        frame3=Frame(self._root)
        frame3.config(bg="#F60A40")
        frame3.pack()

        self._button1=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button1))
        self._button1.grid(row=0, column=0)
        self._button2=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button2))
        self._button2.grid(row=0, column=1)
        self._button3=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button3))
        self._button3.grid(row=0, column=2)
        self._button4=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button4))
        self._button4.grid(row=1, column=0)
        self._button5=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button5))
        self._button5.grid(row=1, column=1)
        self._button6=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button6))
        self._button6.grid(row=1, column=2)
        self._button7=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button7))
        self._button7.grid(row=2, column=0)
        self._button8=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button8))
        self._button8.grid(row=2, column=1)
        self._button9=Button(frame3, text=" ", font=("Times", 20, "bold"), bg="#F65A40", fg=
                             "#fff", height=4, width=8, command=lambda : self.btnclick
                             (self._button9))
        self._button9.grid(row=2, column=2)

        frame4=Frame(self._root)
        frame4.config(bg="#F60A40")
        frame4.pack()

        self._restart=Button(frame4, text="Restart", font=("Times", 20, "bold"),
                             bg="#F65A40", fg="#fff", width=20, height=2, command=lambda :
                             self.restart())
        self._restart.pack(pady=(5,5))
        

    #Checking Winner Function
    def winnercheck(self):
        
        if (self._button1["text"]==self._button2["text"]==self._button3["text"]=="X" or
            self._button4["text"]==self._button5["text"]==self._button6["text"]=="X" or
            self._button7["text"]==self._button8["text"]==self._button9["text"]=="X" or
            self._button1["text"]==self._button5["text"]==self._button9["text"]=="X" or
            self._button3["text"]==self._button5["text"]==self._button7["text"]=="X" or
            self._button1["text"]==self._button4["text"]==self._button7["text"]=="X" or
            self._button2["text"]==self._button5["text"]==self._button8["text"]=="X" or
            self._button3["text"]==self._button6["text"]==self._button9["text"]=="X"):
            self.disablebutton()
            messagebox.showinfo("Tic Tac Toe",self._player1input.get() + " Wins")

        elif (self._button1["text"]==self._button2["text"]==self._button3["text"]=="O" or
            self._button4["text"]==self._button5["text"]==self._button6["text"]=="O" or
            self._button7["text"]==self._button8["text"]==self._button9["text"]=="O" or
            self._button1["text"]==self._button5["text"]==self._button9["text"]=="O" or
            self._button3["text"]==self._button5["text"]==self._button7["text"]=="O" or
            self._button1["text"]==self._button4["text"]==self._button7["text"]=="O" or
            self._button2["text"]==self._button5["text"]==self._button8["text"]=="O" or
            self._button3["text"]==self._button6["text"]==self._button9["text"]=="O"):
            self.disablebutton()
            messagebox.showinfo("Tic Tac Toe",self._player2input.get() + " Wins")

        elif self._flag==8:
            messagebox.showinfo("Tic Tac Toe","Tie")
            self.disablebutton()
            

    #Operation of Button Function
    def btnclick(self, button):
        
        if button["text"]==" " and self._bclick==True:
            button["text"]="X"
            self._bclick=False
            self.winnercheck()
            self._flag=self._flag+1

        elif button["text"]==" " and self._bclick==False:
            button["text"]="O"
            self._bclick=True
            self.winnercheck()
            self._flag=self._flag+1

        else:
            messagebox.showinfo("Tic Tac Toe", "Fill Empty Space")
            

    #Disable the Button Function
    def disablebutton(self):

        self._button1.configure(state=DISABLED)
        self._button2.configure(state=DISABLED)
        self._button3.configure(state=DISABLED)
        self._button4.configure(state=DISABLED)
        self._button5.configure(state=DISABLED)
        self._button6.configure(state=DISABLED)
        self._button7.configure(state=DISABLED)
        self._button8.configure(state=DISABLED)
        self._button9.configure(state=DISABLED)
        

    #Operation of Restart Button Function
    def restart(self):

        self._bclick=True
        self._flag=0
        self.clear()
        self.frames()
        

    #Clear GUI Function
    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()
        
    
obj=TTT()
