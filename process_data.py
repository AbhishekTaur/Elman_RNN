import pandas as pd

data = pd.read_csv("sample/blackscholes-small-4-8-cleaned.csv")

keys = data.keys()
print("Key\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tValues")

for key in keys:
    print(key, "\t\t\t\t\t\t\t\t\t\t\t\t\t", data[key].values[0])


