
try: 
    k = 5//0 
    print(k) 
   
except ZeroDivisionError:    
    print("Can't divide by zero") 
       
finally: 

    print('This is always executed')  
