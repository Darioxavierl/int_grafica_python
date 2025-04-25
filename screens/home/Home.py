import tkinter as tk

from screens.home.homefunc import HomeFunc as funcionalidad


class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Se cargan los widgets iniciales
        self.init_widgets()
    
    def init_widgets(self):
        '''
        Metodo que inicializa los widgets de la pantalla Home
        '''
        # Frame para el titulo
        General_frame = tk.Frame(self)
        #General_frame.configure(background=self.style.BACKGROUND_COLOR)
        General_frame.pack(
            side=tk.TOP,
            expand=True,
            fill=tk.BOTH
        )
        # Label con el titulo de la pantalla
        tk.Label(
            General_frame,
            text="Titulo",
            justify=tk.CENTER,
            #**self.style.STYLE
        ).pack(
            side=tk.LEFT,
            fill = tk.BOTH,
            expand=True
        )    