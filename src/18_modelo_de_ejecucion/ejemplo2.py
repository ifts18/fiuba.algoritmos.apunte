
def fun1(a):
    print a+1

def fun2(b):
    fun1 (b+5)
    print "Volvio a fun2"

fun2(43)
