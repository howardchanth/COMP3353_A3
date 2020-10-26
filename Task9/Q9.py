import numpy as np
import pandas as pd

def distinct_k_mers(k):
    with open("inputQ9.txt", "r") as file:
        k_mers = []
        while True:
            line = file.readline()

            if not line:
                break

            for i in range(len(line) - k):
                k_mers.append(line[i:i+k])

        # Remove duplicates
        k_mers = list(dict.fromkeys(k_mers))

        return k_mers


k = 3
k_mers = distinct_k_mers(k)
print(f"The distinct k-mers (k={k}) are:\n{k_mers}\n")

# Obtain nodes for the De Brujin Graph

nodes = []
for k_mer in k_mers:
    nodes.append(k_mer[:-1])
    nodes.append(k_mer[1:])

# Remove duplicates
nodes = list(dict.fromkeys(nodes))

# Construct De Brujin Graph in the form of adjacency matrix
de_brujin = np.zeros((len(nodes), len(nodes)), dtype=int)
de_brujin = pd.DataFrame(de_brujin, index=nodes, columns=nodes)
for k_mer in k_mers:
    left = k_mer[:-1]
    right = k_mer[1:]
    de_brujin[right][left] += 1

print("The De Brujin matrix is (Assuming A[i][j] is node i to node j):")
print(de_brujin)
