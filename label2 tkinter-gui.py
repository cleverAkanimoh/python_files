import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        
        self.label_text = "Select Any Button"
        self.label = tk.Label(self, text=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)
            
        hello_button = tk.Button(self, text="Hello User",
                                 command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        
        goodbye_button = tk.Button(self, text="Goodbye User",
                                   command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_hello(self):
        self.label_text = "Welcome user"
        
    def say_goodbye(self):
        self.label_text="Goodbye! \n (Closing in 3 seconds)"
        self.after(3000, self.destroy)


        self.label_text = tk.StringVar() 
        self.label_text.set("Select Any Button")

        def say_hello(self):
            self.label_text.set= "Welcome user"

        def say_goodbye(self):
            self.label_text.set="Goodbye! \n (Closing in 3 seconds)"
            self.after(3000, self.destroy)
   
        
if __name__ == "__main__":
    window = Window()
    window.mainloop() 
