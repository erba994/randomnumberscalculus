import timeit
import main
import helpers

import_module = "import main"
testcodeyes = """
def test():
    print('Testo 20 numeri da 1 a 5')
    xlist = helpers.NumberList(20,1,5)
    print('Test con threading')
    main.ThreadOperands(3,xlist).dothework_threading()
    print('Test senza threading')
    main.ThreadOperands(3,xlist).dothework_threading()
"""
testcodeno = """
def test():
    print('Testo 20 numeri da 1 a 5')
    xlist = helpers.NumberList(20,1,5)
    print('Test con threading')
    main.ThreadOperands(3,xlist).dothework_nothreading()
    print('Test senza threading')
    main.ThreadOperands(3,xlist).dothework_nothreading()
"""


if __name__ == '__main__':
    print('tempo con threading: ' + str(timeit.timeit(stmt=testcodeyes, setup=import_module)))
    print('tempo senza threading: ' + str(timeit.timeit(stmt=testcodeno, setup=import_module)))
