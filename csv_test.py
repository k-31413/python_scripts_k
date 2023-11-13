import csv
import os



print("===============Script is starting==================")
print("with using csv lib")


with open('temp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        #print("debug",row[1],":",row[2])
        '''if row[1] == "3":
                print("found it", row[1])
        else:
            print("not found it", row[1])
        '''
        
print("===============Script is ending==================")

print("\n==============================================")
print("File handling starting")
print("==============================================")
path = os.getcwd()

file1 = open('kiran.txt', 'w')
#L = "This is Delhi \n", "This is Paris \n", "This is London \n"
L = "This is Delhi, This is Paris, This is London"
s = "Hello\n"
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
'''
MyString1 = "A geek in need is a geek indeed"
  
if "need" in MyString1: 
    print("Yes! it is present in the string") 
else: 
    print("No! it is not present") 
'''
search_str = 'Paris'

print (L)
if search_str in L:
    print(search_str,"present in the list replacing with Bombay")
    L = L.replace("Paris", "Bombay")
else:
    print(search_str,  "is not present in the list")
    

file1.writelines(L)
 
# Closing file
file1.close()
print("\n==============================================")
print("Checking if the data is written to file or not")
print("==============================================")
file1 = open('kiran.txt', 'r')
print(file1.read())
file1.close()