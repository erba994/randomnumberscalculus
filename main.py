import helpers
import copy


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
