import tkinter as tk

c = 0

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("500x200")
                
        label_username = tk.Label(self, text='username')
        btn_login = tk.Button(self, text='login')

        label_username.pack()
        btn_login.pack()

app = App()
app.mainloop()

# # Create a window object
# window = tk.Tk()

# label_username = tk.Label(window, text='username')
# btn_login = tk.Button(text='login')

# label_username.pack()
# btn_login.pack()


# # Run the event loop
# window.mainloop()