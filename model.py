import random

#model --> contiene logica del gioco
class Model(object):
    def __init__(self):
        self._numMax=100
        self._tentMax=6
        self._tent= self._tentMax
        self._segreto = None

    @property #solo get perchè non voglio che qualcuno dall'esterno setta
    def numMax(self):
        return self._numMax

    @property
    def tentMax(self):
        return self._tentMax

    @property
    def tent(self):
        return self._tent

    @property
    def segreto(self):
        return self._segreto

    def reset(self):
        self._segreto = random.randint(0,self._numMax)
        self._tent = self._tentMax #hai di nuovo tutte le vite
        print(self._segreto)

    def play(self, guess):
        """
        Funziona che esegue uno step del gioco
        :param self: int
        :param guess: -1 se il segreto + più piccolo, 0 se hai vinto, 1 se il segreto è più grande, 2 se hai perso
        :return: -1, 0, 1, 2
        """
        self._tent -= 1
        if guess == self._segreto:
            return 0 #ho vinto, potrei anche mettere una string
        elif self._tent == 0:
            return 2 #ho perso, ho finito le vite
        elif guess > self._segreto:
            return -1 #il segreto è più piccolo
        elif guess < self._segreto:
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




