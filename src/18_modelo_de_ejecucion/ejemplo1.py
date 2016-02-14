
def f():
    x = 50
    a = 20
    print "En f, x vale", x

def g():
    x = 10
    b = 45
    print "En g, antes de llamar a f, x vale", x
    f()
    print "En g, después de llamar a f, x vale", x

g()
