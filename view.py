import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2025 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero", color="blue", size=24)

        #OUT: elementi grafici quando vogliamo dare un info all'utente --> computer verso utente
        #NMAX e TMAX li conosco una volta che lancio il programma --> controller
        self.txtOutNMax = ft.TextField(label="Numero Max", disabled=True, width=200, value=self._controller.getNumMax()) #qualcuno dovrà dire al modello chi è il N Max
        self.txtOutTMax = ft.TextField(label="Tentativi Max", disabled=True, width=200, value=self._controller.getTentMax() )
        self.txtOutTent = ft.TextField(label="Tentativi rimanenti", disabled=True, width=200 )

        #IN: Quando vogliamo prendere delle info dall'utente -> utente verso computer
        self.txtIn = ft.TextField(label="Tentativo", width=200, disabled=True )
        self.btnReset = ft.ElevatedButton(text="Nuova Partita", width=200, on_click=self._controller.reset)
        self.btnPlay = ft.ElevatedButton(text="Gioca", width=200, on_click=self._controller.play, disabled=True )

        self._lv = ft.ListView(expand=True) #permette di scorrere nella finestra --> listino per leggere

        row1 = ft.Container(self._titolo, alignment=ft.alignment.center)
        row2 = ft.Row( [self.txtOutNMax, self.txtOutTMax, self.txtOutTent], alignment=ft.MainAxisAlignment.CENTER) #+azioni --> allineamento diverso
        row3 = ft.Row( [self.btnReset, self.txtIn, self.btnPlay], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, row3, self._lv)
        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()