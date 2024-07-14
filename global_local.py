a=1
def f():
    print("It is global a ",a)
def g():
    a=3
    print("It is local a ",a)
def h():
    global a
    a=5
    print("Redefining a ",a)
    
f()
g()
h()