import tkinter as tk
from model import Model
from view import View
from kontroller import Kontroller

if __name__ == "__main__":
    app = tk.Tk()

    # Loome mudeli, vaate ja kontrolleri
    model = Model()
    kontroller = Kontroller(model)  # Saatke mudel kontrollerisse
    view = View(app, kontroller)  # Saatke kontroller vaatesse

    app.mainloop()