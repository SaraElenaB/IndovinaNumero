from math import log2

from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNumMax(self):
        return self._model._numMax

    def getTentMax(self):
        return self._model._tentMax

    def reset(self, e): #e --> parametro evento che ha senso quando premi il metodo on_click
        self._model.reset()
        self._view.txtOutTent.value = self._model._tent
        self._view._lv.controls.clear() #pulisi l'interfaccia e tutte le vecchie cose scritte
        self._view._lv.controls.append( ft.Text("Indovina a quale numero sto pensando!"))

        self._view.btnPlay.disabled = False
        self._view.txtIn.disabled = False  #manca ancora il numero segreto
        self._view.update()

    def play(self, e):
        tentativoStr = self._view.txtIn.value
        self._view.txtIn.value = "" #cosi non rimane fisso nello schermo quale numero che hai scritto
        self._view.txtOutTent.value = self._model._tent-1

        if tentativoStr == "":
            self._view._lv.controls.append( ft.Text("Attnezione! Inserisci un valore numerico da testare", color="red"))
            self._view.update()
            return #non ha senso andare avanti

        try:
            tentativoInt = int(tentativoStr) #può fallire nel caso ci sia un num decimale ad es
        except ValueError:
            self._view._lv.controls.append( ft.Text("Attenzione! Il valore inserito non è un intero, riprovare!", color="red"))
            return

        risultato = self._model.play(tentativoInt) #vale 1,-1,0,2
        if risultato==0:
            self._view._lv.controls.append( ft.Text(f"Fantastico, hai vinto, il segreto era {self._model._segreto}", color="green"))
            self._view.btnPlay.disabled = True
            self._view.txtIn.disabled = True
            self._view.update()
            return

        elif risultato==2:
            self._view._lv.controls.append( ft.Text(f"Mi dispiace, hai finito le vite, il segreto era {self._model._segreto}",color="black"))
            self._view.btnPlay.disabled = True
            self._view.txtIn.disabled = True
            self._view.update()
            return

        elif risultato == -1:
            self._view._lv.controls.append( ft.Text(f"Ci sei quasi, il segreto è più piccolo di {self._view.txtIn.value}", color="black"))
            self._view.update()
            #no return perchè devi continuare a giocare

        else: #risultato=1
            self._view._lv.controls.append( ft.Text(f"Ci sei quasi, il segreto è più grande di {self._view.txtIn.value}", color="black"))
            self._view.update()



#non va a considerare l'utlimo caso

