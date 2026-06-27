import tkinter as tk
from tkinter import ttk

class FormView:
    def __init__(self, root):
        self.root = root
        style = ttk.Style()
        style.theme_use('clam') 
        # Main Frame
        style.configure("Red.TFrame", background="red")
        self.frame = ttk.Frame(self.root, height=100, style="Red.TFrame")
        self.frame.pack(fill="both", padx=(30, 200), pady=40)
        
        # Title
        style.configure("Title.TLabel", background="yellow")
        self.title = ttk.Label(self.frame, width="40", style="Title.TLabel", text="hello", anchor="c")
        self.title.pack()
        
        my_obj = tk.StringVar()
        def update_dic(*args):
            print("my_obj==>>", my_obj.get())
        my_obj.trace_add("write", update_dic)
        
        def change(event):
            print("event ->", event.widget.get())
        # Input Filed
        style.configure("Entry.TEntry", fieldbackground="green", foreground='red')
        self.entry = ttk.Entry(self.frame, style="Entry.TEntry", textvariable=my_obj)
        self.entry.pack()
        self.entry.bind("<Key>", change)
        print("my_obj -->>", my_obj)
        
        
        # 
import tkinter as tk
from tkinter import ttk

