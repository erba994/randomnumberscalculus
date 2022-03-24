import concurrent.futures
import random


class NumberList:

    def __init__(self, length, minimum, maximum):
        self.itemlist = [random.randint(minimum, maximum) for i in range(length)]

    def __str__(self):
        return f"la lista è: {', '.join([str(x) for x in self.itemlist])}"



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


class ThreadWorkers:

    def __init__(self,threadnum,func):

        with concurrent.futures.ThreadPoolExecutor(max_workers=threadnum) as executor:
            executor.submit(func)



if __name__ == "__main__":
    pass

