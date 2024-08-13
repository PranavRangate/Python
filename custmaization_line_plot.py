import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,20,25,30]

plt.plot(x,y,color='green',linestyle='--',linewidth=2,marker='o',markerfacecolor='red')

plt.title('simple line graph')
plt.xlabel('values of x')
plt.ylabel('values of y')

plt.show()