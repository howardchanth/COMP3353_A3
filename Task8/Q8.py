from itertools import product

with open("input.txt", "r") as file:
    s = file.readline()
    n = int(file.readline())

s = s.split()

s = list(product(s, repeat=n))

for i, string in enumerate(s):
    string = list(string)
    string = "".join(string)
    s[i] = string

with open("output.txt", "w") as file:
    for string in s:
        print(string, file=file)