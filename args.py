def myf(*arg,**kwargs):
    print("Arg:",arg)
    print("kargs:",kwargs)
myf('first','second','third',first="first",second='second',third="third")