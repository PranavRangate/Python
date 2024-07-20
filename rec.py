def show(n):
    if(n==0):  #to stop the recurtion
      return
    print(n)   #base 
    show(n-1)  #recurtion
show(5)