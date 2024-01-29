import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.geometry("500x450")
root.title("Todo List")
root.config(bg="#111111")
root.iconbitmap(r"D:\Dev\python programme\todolist\right-6229287.ico")

def task_add():
    try:
        task = task_entry.get()

        if task != "":
            if task == "Aufgabe eingeben                    ":
                mb.showwarning('Fehler', 'Bitte eine Aufgabe eingeben')
            else:
                task_list.insert(tk.END, task)
                task_entry.delete(0, 'end')
        else:
            mb.showerror('Error', 'Bitte eine Aufgabe eingeben')
    except:
        mb.showerror('Error', 'Bitte melde diesen Error an momo.itsystems@gmail.com')

def task_remove():
    try:
        task_list.delete(tk.ANCHOR)
    except:
        mb.showerror('Error', 'Bitte melde diesen Error an momo.itsystems@gmail.com')
def clear_entry(event, entry):
    try:
        entry.delete(0, tk.END)
    except:
        mb.showerror('Error', 'Bitte melde diesen Error an momo.itsystems@gmail.com')


frame = tk.Frame(root)
frame.pack(pady=10)

task_list = tk.Listbox(frame, width=25, height=8, font=('Times', 18), fg="#464646", selectbackground="#333333", activestyle="none")

task_list.pack(side=tk.LEFT, fill=tk.BOTH)

scroll_bar = tk.Scrollbar(frame)
scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_list.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=task_list.yview)

task_entry = tk.Entry(root, font=('Times', 24))
task_entry.insert(0, 'Aufgabe eingeben                    ')
task_entry.bind('<Button-1>', lambda event: clear_entry(event, task_entry))
task_entry.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

task_add_btn = tk.Button(button_frame, text='Aufgabe hinzufügen', font=('Times', 14), bg='green', fg='white', padx=20, pady=10 , command=task_add)
task_add_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

task_remove_btn = tk.Button(button_frame, text='Aufgabe entfernen', font=('Times', 14), bg='red', fg='white', padx=20, pady=10 , command=task_remove)
task_remove_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

root.mainloop()