import csv

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
        #print(row)
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
