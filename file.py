with open("practice.txt","w") as f:           #bye directly using 'w' it can create the new practice file
    f.write("Hi everyone\nWe are learning file i/o\nusing python\ni like programming")


with open("practice.txt","r") as f:          #read the file and replacing the java into python and store in new_data
    data=f.read()
    new_data = data.replace("java","python")
    print(new_data)

with open("practice.txt","w") as f:        #overwrite this new_data in practice.txt file
    f.write(new_data)