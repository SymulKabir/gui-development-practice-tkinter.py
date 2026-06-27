import tkinter as tk
from tkinter import ttk
from app.ui.formView import FormView



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("This is practice app")
        screen_width = self.root.winfo_screenwidth()
        app_height = 1000
        app_width = 650
        y_position = 0
        x_position = screen_width - app_width
        
        print("screen_width", screen_width)
        self.root.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
        FormView(self.root)
        
        

        
print("__name__->", __name__)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    print("app", app)
    root.mainloop()