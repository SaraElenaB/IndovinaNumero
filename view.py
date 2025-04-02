import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2025 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        #OUT: elementi grafici quando vogliamo dare un info all'utente --> computer verso utente
        #NMAX e TMAX li conosco una volta che lancio il programma --> controller
        self.txtOutNMax = ft.TextField(label="Numero Max", disabled=True, width=200,
                                       value=self._controller.getNumMax()) #qualcuno dovrà dire al modello chi è il N Max
        self.txtOutTMax = ft.TextField(label="Tentativi Max", disabled=True, width=200,
                                       value=self._controller.getTentMax())
        self.txtOutTent = ft.TextField(label="Tentativi rimanenti", disabled=True, width=200 )


        #IN: Quando vogliamo prendere delle info dall'utente -> utente verso computer
        self.txtIn = ft.TextField(label="Tentativo", width=200, disabled=True )
        self.btnReset = ft.ElevatedButton(text="Nuova Partita", width=200,
                                          on_click=self._controller.reset)
        self.btnPlay = ft.ElevatedButton(text="Gioca", width=200,
                                         on_click=self._controller.play, disabled=True )

        self._lv = ft.ListView(expand=True) #permette di scorrere nella finestra --> listino per leggere

        row1 = ft.Container(self._titolo, alignment=ft.alignment.center)
        row2 = ft.Row( [self.txtOutNMax, self.txtOutTMax, self.txtOutTent],
                       alignment=ft.MainAxisAlignment.CENTER) #+azioni --> allineamento diverso
        row3 = ft.Row( [self.btnReset, self.txtIn, self.btnPlay],
                       alignment=ft.MainAxisAlignment.CENTER)


        #estensione 2: barra tentativi che si aggiorna
        self._pb = ft.ProgressBar(width=600, color="amber")


        #estensione 3: livello di difficoltà
        #    devi separare i due componenti:
        #            1. imposta lo slider --> chiamato solo all'inizio
        #            2. imposta l'handler "on_change" fuori dal costruttore, dove viene chiamata ogni volta la funzione e svolta
        self._titoloDifficolta= ft.Text( "Seleziona difficoltà", size=16) #è sbagliato mettere width?
        self._slider_difficolta = ft.Slider(
                              min=1, max=3, divisions=2,
                              label="{value}")
                              #on_change= self._controller.setDifficulty --> dovresti poi inizializzare con una riga
                              #sucessiva con --> self._controller.setDifficulty(None)
        self._slider_difficolta.on_change = self._controller.setDifficulty
        self._livelloSelezionato = ft.Text("Facile", size=14)
        self._slider_difficolta.value = 1 #Facile di default

        rowDiff = ft.Column( [self._titoloDifficolta,
                              ft.Row([self._slider_difficolta , self._livelloSelezionato],
                             alignment=ft.MainAxisAlignment.CENTER)
                              ])

        self._page.add(row1, row2, row3, rowDiff, self._pb, self._lv)
        self._page.update()

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def setController(self,controller):
        self._controller = controller

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def update(self):
        self._page.update()