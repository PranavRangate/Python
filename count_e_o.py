e_count = 0
o_count = 0
with open("num.txt","r") as f:
    data = f.read()  
#    num=""
#    for i in range(len(data)):
#        if(data[i]==","):
#           print(int(num))
#           if(int(val) % 2 == 0 ):
#              e_count+=1
#           else:
#              o_count+=1
#            num=""
#        else:
#            num+=data[i]
    nums=data.split(",")
    print(nums)
    
    for val in nums:
        if(int(val) % 2 == 0 ):
           e_count+=1
        else:
            o_count+=1
print("count of even no. is ",e_count)
print("count of odd no. is ",o_count)
            