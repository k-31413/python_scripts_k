import os

# print files in present dir before creating file2 
print("List of files before")
print(os.listdir())
print("\n")

#open file1 in reading mode
file1 = open('template_sv.txt', 'r')

#open file2 in writing mode
file2 = open('file2.txt','w')

#read from file1 and write to file2
for line in file1:
    file2.write(line)

#close file1 and file2
file1.close()
file2.close()

#open file2 in reading mode
file2 = open('file2.txt','r')

#print the file2 content
print(file2.read())

#close the file2
file2.close()

#print the files after creating file2, check the output
print("\n")
print("List of files after")
print(os.listdir())
print("\n")
