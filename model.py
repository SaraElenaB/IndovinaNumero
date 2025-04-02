import random

#model --> contiene logica del gioco
class Model(object):
    def __init__(self):
        self._numMax=100
        self._tentMax=6
        self._tent= self._tentMax
        self._segreto = None

        #estensione 4:
        self._minRange=0
        self._maxRange= self._numMax

        #estensione 5:
        self._tentPrecedenti = []

    # ---------------------------------------------------------------------------------------------------------------------------------------
    #problema iniziale --> dovevo avere dei valori che l'utente non può modificare: uso solo getter
    #estensione 3 --> devo modificare in base alla difficoltà il numMax e i tentMax
    @property
    def numMax(self):
        return self._numMax

    @numMax.setter
    def numMax(self, value):
        self._numMax = value

    @property
    def tentMax(self):
        return self._tentMax

    @tentMax.setter
    def tentMax(self, value):
        self._tentMax = value

    @property
    def tent(self):
        return self._tent

    @property
    def segreto(self):
        return self._segreto

    @property #fondamentale per leggere nell'interfaccia
    def currentRange(self):
        return (self._minRange, self._maxRange)

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def reset(self):
        self._segreto = random.randint(0,self._numMax)
        self._tent = self._tentMax #hai di nuovo tutte le vite

        self._minRange = 0
        self._maxRange = self._numMax

        self._tentPrecedenti = []
        print(self._segreto) #print??

    # ---------------------------------------------------------------------------------------------------------------------------------------
    def play(self, guess):
        """
        Funziona che esegue uno step del gioco
        :param guess: -1 se il segreto + più piccolo, 0 se hai vinto, 1 se il segreto è più grande, 2 se hai perso
        :return: -1, 0, 1, 2
        """
        if guess in self._tentPrecedenti:
            return None

        self._tentPrecedenti.append(guess)
        self._tent -= 1  #fondamentale per aggiornare i tentativi
        if guess == self._segreto:
            return 0 #ho vinto, potrei anche mettere una string
        elif self._tent == 0:
            return 2 #ho perso, ho finito le vite
        elif guess > self._segreto:
            self._maxRange = min(self._maxRange, guess-1)
            return -1 #il segreto è più piccolo
        elif guess < self._segreto:
            self._minRange = max(self._minRange, guess+1)
            return 1

# if __name__ == '__main__': #se la variabile è uguale, stiamo eseguendo il modello
#     m = Model()
#     m.reset()
#     print(m.play(50))
#     print(m.play(10))
#     print(m.play(20))
#     print(m.play(15))
#     print(m.play(13))
#     #era 11




