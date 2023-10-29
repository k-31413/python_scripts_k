import yaml

with open('ex.yaml') as file:
    try:
        data = yaml.safe_load(file)
        print("---------------------------------------------------------")
        print("no if items in data variable", ":", len(data))
        print("---------------------------------------------------------")
        print(" items in dict format data variable", ":", data.items())
        print("---------------------------------------------------------")
        print("printdata before ", ":", data)

        print("---------------------------------------------------------")
        for key, value in data.items():
            print("seperation wrt ky value pair -->", key, ":", value)

    except yaml.YAMLError as exception:
        print(exception)
