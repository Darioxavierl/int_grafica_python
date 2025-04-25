import tkinter as tk

# importar contantes de configuracion
# importar pantallas 
import screens.home.Home as home

from ctypes import windll

class manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(args, **kwargs)

        container = tk.Frame(self)

        # Ventana contenedora
        self.title("titulo")
        # Convirtiendo la aplicacion para que no use el escalado de windows 
        windll.shcore.SetProcessDpiAwareness(1)
        self.geometry("1200x500")
        #self.overrideredirect(True)
        self.state('zoomed')

        #container.configure(background = style.BACKGROUND_COLOR)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )

        self.frames = {}
        
        
        for F in (home.Home,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky=tk.NSEW)
        self.show_frame(home.Home)

        

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()