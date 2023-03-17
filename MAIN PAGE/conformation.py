from tkinter import messagebox

class confomation:
    def info_show(data):
        return messagebox.showinfo("INFO-Coformation window....",message=data)
    def warning_alart(data):
        return messagebox.showwarning("Warning/alert window",message=data)
    def info_conformation(data):
        return messagebox.askyesno("INFO-Coformation window....",message=data)

        