from math import log2

from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    #---------------------------------------------------------------------------------------------------------------------------------------
    def getNumMax(self):
        return self._model._numMax

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def getTentMax(self):
        return self._model._tentMax

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def reset(self, e): #e --> parametro evento che ha senso quando premi il metodo on_click
        self._model.reset()
        self._view.txtOutTent.value = self._model._tent
        self._view._lv.controls.clear() #pulisi l'interfaccia e tutte le vecchie cose scritte
        self._view._lv.controls.append( ft.Text("Indovina a quale numero sto pensando!"))

        self._view.btnPlay.disabled = False
        self._view.txtIn.disabled = False  #manca ancora il numero segreto

        self._view._pb.value = self._model.tent / self._model.tentMax
        self._view.txtOutTent.value = self._model.numMax

        self._view.update()

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def setDifficulty(self, e):

        livello = int(self._view._slider_difficolta.value)

        #mappa i livelli a parametri di gioco:
        if livello == 1:
            self._model.numMax = 50
            self._view._livelloSelezionato.value = "Difficoltà: Facile"
        if livello == 2:
            self._model.numMax = 100
            self._view._livelloSelezionato.value = "Difficoltà: Media"
        if livello == 3:
            self._model.numMax = 500
            self._view._livelloSelezionato.value = "Difficoltà: Difficile"

       #imposta arrotondamento per eccesso con il +1
        self._model.tentMax = int(log2(self._model.numMax)) + 1 #arrotonda per eccesso

        #aggiorna la vista
        self._view.txtOutNMax.value = self._model.numMax
        self._view.txtOutTMax.value = self._model.tentMax
        self._view.update()

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def play(self, e):
        tentativoStr = self._view.txtIn.value
        self._view.txtIn.value = ""           #cosi non rimane fisso nello schermo quale numero che hai scritto

        #controlli generali:
        if tentativoStr == "":
            self._view._lv.controls.append( ft.Text("Attenzione! Inserisci un valore numerico da testare",
                                                    color="red") )
            self._view.update()
            return #non ha senso andare avanti

        try:
            tentativoInt = int(tentativoStr) #può fallire, ad es nel caso ci sia un num decimale
        except ValueError:
            self._view._lv.controls.append( ft.Text("Attenzione! Il valore inserito non è un intero, riprovare!",
                                                    color="red"))
            self._view.update()
            return

        if tentativoInt < 0 or tentativoInt > self._model.numMax:
            self._view._lv.controls.append( ft.Text(f"Attenzione, valore inserito non è compreso tra 0 e {self._model.numMax}.",
                                                    color="red"))
            self._view.update()
            return


        #estensione 4:
        if tentativoInt < self._model._minRange or tentativoInt > self._model._maxRange:
            self._view._lv.controls.append(ft.Text(f"Attenzione! Il numero deve essere tra {self._model._minRange} e {self._model._maxRange}",
                                                   color="red"))
            self._view.update()
            return

        # estensione 5:
        if tentativoInt in self._model._tentPrecedenti:
            self._view._lv.controls.append(ft.Text("Hai già provato questo numero! Prova con un altro.",
                                                    color="orange"))
            self._view.update()
            return

        self._view.txtOutTent.value = self._model.tent -1  #serve per aggiornare il txtOutTent che altrimenti ha numeri a caso
        self._view._pb.value = (self._model.tent - 1) / self._model.tentMax #estensione 2


        #gioco effettivo:
        risultato = self._model.play(tentativoInt) #vale 1,-1,0,2
        minR, maxR = self._model.currentRange
        rangeText = f"Intervallo corrente: {minR} - {maxR}"  #è quello che mi conpare nell'interfaccia

        if risultato==0:
            self._view._lv.controls.append( ft.Text(f"Fantastico, hai vinto! Il segreto era {self._model._segreto}",
                                                    color="green"))
            self._view._lv.controls.append( ft.Text(rangeText), color="amber")
            self._view.btnPlay.disabled = True
            self._view.txtIn.disabled = True
            self._view.update()
            return

        elif risultato==2:
            self._view._lv.controls.append( ft.Text(f"Mi dispiace, hai finito le vite, il segreto era {self._model._segreto}",
                                                    color="black"))
            self._view._lv.controls.append(ft.Text(rangeText))
            self._view.btnPlay.disabled = True
            self._view.txtIn.disabled = True
            self._view.update()
            return

        elif risultato == -1: #segreto è + piccolo
            self._view._lv.controls.append( ft.Text(f"Ci sei quasi, il segreto è più piccolo di {tentativoInt}.",
                                                    color="black"))
            self._view._lv.controls.append(ft.Text(rangeText))
            self._view.update()
            #no return perchè devi continuare a giocare

        else: #risultato=1
            self._view._lv.controls.append( ft.Text(f"Ci sei quasi, il segreto è più grande di {tentativoInt}",
                                                    color="black"))
            self._view._lv.controls.append(ft.Text(rangeText))
            self._view.update()

        #aggiorna gli elementi
        self._view.txtOutTent.value = self._model.tent
        self._view._pb.value = self._model._tent / self._model._tentMax
        self._view.update()


