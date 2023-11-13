import csv
import os


#path = 'c:\\temp\\'

#file=open( path +"xyz.CSV", "r")
#reader = csv.reader(file)
#for line in reader:
#    t=line[1],line[2]
print("===============Script is starting==================")
#import csv


#import pandas

# reading the CSV file
#csvFile = pandas.read_csv('temp.csv')

# displaying the contents of the CSV file
#print(csvFile)

# opening the CSV file
#with open('temp.csv', mode ='r')as file:
#    csvFile = csv.reader(file)

# displaying the contents of the CSV file
"""
print("without using csv lib")
file = open('temp.csv', 'r')
for line in file:
   print("---------------",line)
    # file is closed here
#    file.close()
#for lines in csvFile:
#		print(lines)

"""
print("with using csv lib")


with open('temp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        #print("debug",row[1],":",row[2])
        if row[1] == "3":
                print("found it", row[1])
        else:
            print("not found it", row[1])
        
        

print("------------Method 3 with using csv lib")  
      
"""
with open('temp.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
 """
print("===============Script is ending==================")


print("file handling Script is starting now")

path = os.getcwd()
"""
path += "\kiran.txt"

#path = path.replace('\', '/'')

string_with_backslash = path
string_with_forwardslash = string_with_backslash.replace("\\", "/")
print("k_print", string_with_forwardslash)

print("full path is ", path)  
# Check whether the specified 
# path exists or not 
isExist = os.path.exists(path) 
isExist2 = os.path.exists(string_with_forwardslash) 



print(isExist)
print(isExist2)

newpath =path.replace("kiran.txt", "")
print("newpath", newpath)
isdir = os.path.isdir(newpath) 
print(isdir)


#temp_path = "C:/Users/V/Desktop/ELEC.jpg"
temp_path = "E:/PYTHON_SCRIPTS BASICS/python_scripts_k/kiran.txt"
isfile = os.path.isfile(temp_path)
print(isfile)

"""

file1 = open('kiran.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
file1.writelines(L)
 
# Closing file
file1.close()

print("Checking if the data is written to file or not")
file1 = open('kiran.txt', 'r')
print(file1.read())
file1.close()