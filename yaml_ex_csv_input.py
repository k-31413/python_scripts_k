import yaml


import argparse
 
msg = "Adding description"
 
# Initialize parser
#parser = argparse.ArgumentParser(description = msg)
#parser.parse_args()


# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.Output:
    print("Displaying Output as: % s" % args.Output)

with open('work.yaml') as file:
    try:
        data = yaml.safe_load(file)
        print("---------------------------------------------------------")
        #print("no if items in data variable", ":", len(data))
        #print("---------------------------------------------------------")
        #print(" items in dict format data variable", ":", data.items())
        #print("---------------------------------------------------------")
        print("printdata before ", ":", data)

        print("---------------------------------------------------------")
        #for key, value in data.items():
         #   print("seperation wrt ky value pair -->", key, ":", value)

        for key, value in data.items():
            #if key == "K":
            if key == args.Output.upper():
                print("FOUND_IT-Key:",key,"value:\n",value)
            else:
                print("NOT_FOUND_Key:",key,"value:", value)
    except yaml.YAMLError as exception:
        print(exception)
