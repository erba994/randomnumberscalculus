import concurrent.futures
import random
import collections

"""
ho separato le classi di supporto dalla classe principale che rappresenta la business
logic tramite il file helpers che vado a richiamare sul main
"""


""" 
classe che genera la lista di numeri, ho scelto una deque per garantire migliori
tempi di accesso in caso di grandi numeri o implementazioni future sulla logica di
threading
"""

class NumberList:

    def __init__(self, length, minimum, maximum):
        self.itemlist = collections.deque([random.randint(minimum, maximum) for i in range(length)])

    def __str__(self):
        return f"la lista è: {', '.join([str(x) for x in self.itemlist])}"


"""
le tre classi di operatori contengono al loro interno in inizializzazione lo stato
della somma, hanno l'operando relativo come callable e ritornano il risultato in forma 
descrittivase stampati
"""

class OperandSum:

    def __init__(self):
        self.sumtotal = 0

    def __call__(self, x):
        self.sumtotal += x

    def __str__(self):
        return f"la somma è: {str(self.sumtotal)}"

class OperandSumSquare:

    def __init__(self):
        self.sumsquaretotal = 0

    def __call__(self, x):
        self.sumsquaretotal += x**2

    def __str__(self):
        return f"la somma dei quadrati è: {str(self.sumsquaretotal)}"


class OperandMultiply:

    def __init__(self):
        self.summultiplytotal = 1

    def __call__(self, x):
        self.summultiplytotal *= x

    def __str__(self):
        return f"il prodotto è: {str(self.summultiplytotal)}"

"""
questa classe invoca il processo di threading, ThreadPoolExecutor tiene conto automaticamente
della gestione del lock attraverso i tre thread dichiarati con max_workers
"""
class ThreadWorkers:

    def __init__(self,threadnum,func):

        with concurrent.futures.ThreadPoolExecutor(max_workers=threadnum) as executor:
            executor.submit(func)



if __name__ == "__main__":
    pass

