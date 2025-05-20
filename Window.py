import tkinter as tk
from tkinter import *
from tkinter import messagebox
import gc
import sys

class GUI_App():
    def __init__(self):
        GUI_App.start_window()
    
    @staticmethod
    def update_total():
        try:
            sq = int(GUI_App.SQ_amount_box.get()) if GUI_App.SQ_amount_box.get() else 0
            sq_frag = int(GUI_App.SQFrag_amount_box.get()) if GUI_App.SQFrag_amount_box.get() else 0
            tickets = int(GUI_App.tickets_amount_box.get()) if GUI_App.tickets_amount_box.get() else 0
            total_from_sq = sq // 3
            total_from_frag = sq_frag // 21
            total = tickets + total_from_sq + total_from_frag
            GUI_App.total_rols_value.config(text=str(total))
        except ValueError:
            GUI_App.total_rols_value.config(text="0")

    @staticmethod
    def validate_number(action, value):
        if action == '1':  # Si es una inserción
            return value.isdigit()  # Acepta solo números
        return True
    
    def start_window(window=None):
        try:
            if window is None:
                main_window = tk.Tk()
            GUI_App.generateWindow(main_window,500,300,"Rolls Counter")

            validate_cmd = main_window.register(GUI_App.validate_number)
            
            title = tk.Label(main_window,text='Rolls Counter', bg='papaya whip', font=('Arial',16), wraplength=300, justify='center')
            title.place(relx=0.5, y=25, anchor='center')

            SQ_amount_text = tk.Label(text='Saint Quartz:', font=('Arial',13), bg='papaya whip')
            SQ_amount_text.place(relx=0.25, y=65, anchor='center')
            GUI_App.SQ_amount_box = tk.Entry(main_window, width=10, font=('Arial',13), validate="key", validatecommand=(validate_cmd, '%d', '%P'))
            GUI_App.SQ_amount_box.place(relx=0.25, y=90, anchor='center')
            GUI_App.SQ_amount_box.bind("<KeyRelease>", lambda event: GUI_App.update_total())

            SQFrag_amount_text = tk.Label(text='SQ Fragments:', font=('Arial',13), bg='papaya whip')
            SQFrag_amount_text.place(relx=0.5, y=65, anchor='center')
            GUI_App.SQFrag_amount_box = tk.Entry(main_window, width=10, font=('Arial',13), validate="key", validatecommand=(validate_cmd, '%d', '%P'))
            GUI_App.SQFrag_amount_box.place(relx=0.5, y=90, anchor='center')
            GUI_App.SQFrag_amount_box.bind("<KeyRelease>", lambda event: GUI_App.update_total())

            tickets_amount_text = tk.Label(text='Tickets:', font=('Arial',13), bg='papaya whip')
            tickets_amount_text.place(relx=0.75, y=65, anchor='center')
            GUI_App.tickets_amount_box = tk.Entry(main_window, width=10, font=('Arial',13), validate="key", validatecommand=(validate_cmd, '%d', '%P'))
            GUI_App.tickets_amount_box.place(relx=0.75, y=90, anchor='center')
            GUI_App.tickets_amount_box.bind("<KeyRelease>", lambda event: GUI_App.update_total())

            total_rolls_text = tk.Label(text='Total Rolls:', font=('Arial',15), bg='papaya whip')
            total_rolls_text.place(relx=0.5, y=150, anchor='center')
            GUI_App.total_rols_value = tk.Label(main_window, width=10, text='0', font=('Arial', 20), bg='light goldenrod')
            GUI_App.total_rols_value.place(relx=0.5, y=190, anchor='center')

            exit_btn = tk.Button(main_window, text="Close", font=('Arial',14), command=GUI_App.endProgram)
            exit_btn.place(relx="0.1", rely="0.9", anchor="center")
            #mainloop
            main_window.mainloop()
        except NameError:
            messagebox.showerror('Error',str(NameError))
    
    def generateWindow(window,ancho,alto,titulo):
        try:
            for widget in window.winfo_children():
                widget.destroy()
            gc.collect()
            window.title(titulo)
            window.config(bg='papaya whip')
            window.resizable(False,False)
            window.protocol("WM_DELETE_WINDOW", GUI_App.endProgram)
            window.geometry(f"{ancho}x{alto}+{round(window.winfo_screenwidth()/2 - ancho/2)}+{round(window.winfo_screenheight()/2 - alto/2)}")
            window.grab_set()
            window.focus_set()
        except NameError:
            messagebox.showerror('Error',str(NameError))

    def endProgram():
        try:
            res = messagebox.askquestion("Confirm", "Do you want to close the program?")
            if res == 'yes':
                sys.exit()
        except NameError:
            messagebox.showerror('Error',str(NameError))