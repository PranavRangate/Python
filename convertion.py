print('This is example of tuple:')
tp=(10,20,30,40,50)
print(tp,'\n')

tp=list(tp)
tp.insert(3, 5)
print('After converting tuple into list and adding 5 in 4th pos :')
print(tp,'\n')


print('This is example of set:')
st={10,20,30,40,50,10,10}
print(st,'\n')

st=list(st)
st.insert(3, 5)
print('After converting set into list and adding 5 in 4th pos :')
print(st,'\n')

print('This is example of list:')
ls=[10,20,30,40,50]
print(ls,'\n')

ls=set(ls)
print('After converting list into set :')
print(ls,'\n')