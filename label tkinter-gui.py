import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CRUSH APP')

        self.label=tk.Label(self,text='Select Any Button')
        self.label.pack(fill=tk.BOTH,expand=1,padx=100,pady=30)

        hello_button=tk.Button(self,text='Hello User',
                               command=self.say_hello)
        hello_button.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))

        goodbye_button=tk.Button(self,text='Goodbye',
                              command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))
        
    def say_hello(self):
        self.label.configure(text='Welcome User!')

    import tkinter.messagebox as box
    def say_goodbye(self):
        self.label.configure(text='Goodbye! \n (Closing App in 5 Seconds)')
        box.showinfo('App Will Close In 5 Seconds' )
        self.after(5000,self.destroy)


if __name__=='__main__':
    window=Window()
    window.mainloop()
