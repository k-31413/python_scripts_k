import csv
import os

temp = 0
k_debug_enable = 0

def seperator_fun(fname):
    print("==========================================")
    print(fname)
    print("==========================================")

seperator_fun("Script is starting")

file1 = open('template_sv.txt', 'r')

if k_debug_enable:
    seperator_fun(" opening template_sv.txt in read mode ")

if k_debug_enable:
    seperator_fun(" opening temp_output.txt in read mode ")
#open file2 in writing mode
file2 = open('temp_output.txt','w')

if k_debug_enable:
    seperator_fun(" Iterating in loop to write contents of template_sv to temp_output ")
#read from file1 and write to file2
for line in file1:
    if "check" in line:
        if k_debug_enable:
            text = line
            print("k_Debug_0", text)
       
        with open('signals_list.csv', 'r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                if row[2] == "output":
                        #print("row content :", row)
                        #print("formatted output", line)
                        k1 = line.replace("signal_name", row[0])
                        k2 = k1.replace("signal_value", row[3])
                        #print("formatted output_2", k2)
                        file2.write(k2)
                        file2.write("\n")
            
    else:
        if k_debug_enable:
            print("k_Debug_2", line)
            #break
        file2.write(line)
    

            #file2.write(line)
if k_debug_enable:
    seperator_fun(" closing both opened files ")
#close file1 and file2
file1.close()
file2.close()

seperator_fun(" opening temp_output.txt ")
#open file2 in reading mode
file2 = open('temp_output.txt','r')

seperator_fun(" reading contents of temp_output.txt ")
#print the file2 content
print(file2.read())

seperator_fun("closing temp_output.txt ")
#close the file2
file2.close()

print("===============Script is ending==================")
