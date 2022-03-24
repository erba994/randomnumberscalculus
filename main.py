import helpers
import copy

"""
qui abbiamo la classe principale:
vengono inizializzati gli operatori che contengono il risultato delle operazioni e poi
viene generata tramite initialqueue la lista di numeri, che poi copio subito come deepcopy 
per il numero di operazioni in modo che ogni operando acceda ad una lista separata 
in fase di pop mentre svolge i calcoli (altrimenti il primo operatore svuoterebbe la lista
per tutti).

operandthread svolge l'operazione di ottenimento numero dalla lista e lo da in pasto 
all'operatore che aggiorna il totale interno e poi finita la lista ritorna il risultato
essendo che operandthread non dipende da parametri self l'ho dichiarato come metodo statico
anche se in questa implementazione specifica non è necessario.

le due funzioni dothework implementano la business logic con e senza threading:
- stampa lista dei numeri
- stampa risultato somma
- stampa risultato moltiplicazione
- stampa risultato somma dei quadrati

l'applicazione come main lancia un ciclo di calcolo con threading e stampa il risultato,
nel file di tests vengono invocate entrambe le funzioni con un timeit per il confronto
dei tempi di esecuzione.
"""

class ThreadOperands:

    def __init__(self, threads, numberqueue):
        self.sum = helpers.OperandSum()
        self.sumsquare = helpers.OperandSumSquare()
        self.multiply = helpers.OperandMultiply()
        self.threads = threads
        self.initialqueue = numberqueue
        self.sumqueue = copy.deepcopy(self.initialqueue.itemlist)
        self.sumsquarequeue = copy.deepcopy(self.initialqueue.itemlist)
        self.multiplyqueue = copy.deepcopy(self.initialqueue.itemlist)

    @staticmethod
    def operandthread(numberdeque,operand):
        while len(numberdeque) > 0:
            operand(numberdeque.pop())
        return print(operand)

    def dothework_threading(self):
        print(self.initialqueue)
        helpers.ThreadWorkers(self.threads, self.operandthread(self.sumqueue, self.sum))
        helpers.ThreadWorkers(self.threads, self.operandthread(self.sumsquarequeue, self.sumsquare))
        helpers.ThreadWorkers(self.threads, self.operandthread(self.multiplyqueue, self.multiply))

    def dothework_nothreading(self):
        print(self.initialqueue)
        self.operandthread(self.sumqueue, self.sum)
        self.operandthread(self.sumsquarequeue, self.sumsquare)
        self.operandthread(self.multiplyqueue, self.multiply)


if __name__ == "__main__":
    xlist = helpers.NumberList(20, 1, 5)
    ThreadOperands(3, xlist).dothework_threading()
