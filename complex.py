class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumb(self):
        print(self.real,"i + ",self.img,"j")
        
    def __add__(self,any_num):
        new_real=self.real+any_num.real
        new_img=self.img+any_num.img
        return Complex(new_real,new_img)
    
    def __sub__(self,any_num):
        new_real=self.real-any_num.real
        new_img=self.img-any_num.img
        return Complex(new_real,new_img)
    
n1 = Complex(3,4)
n2 = Complex(1,2)

n3 = n1+n2
n4 = n1-n2

n3.showNumb()
n4.showNumb()