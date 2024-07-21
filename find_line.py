def find_line_no(word):
    data = True
    line_no = 1
    with open("practice.txt","r") as f:    
        while data:
          data=f.readline()
          if(word in data):      #for finding file_no of learning word
            print(line_no)
          line_no += 1
          
find_line_no("learning")