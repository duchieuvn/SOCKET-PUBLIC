import tkinter as tk

c = 0

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("500x200")
        
        #
        container = tk.Frame(self)
        container.configure(bg="red")
        container.pack(side="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        frame = StartPage(container)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


        
        


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg="bisque2")

        label_title = tk.Label(self, text="LOG IN")
        label_user = tk.Label(self, text="username ")
        label_pswd = tk.Label(self, text="password ")

        label_title.pack()
        label_user.pack()
        label_pswd.pack()


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