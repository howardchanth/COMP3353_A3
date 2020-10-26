with open("./input.txt", "r") as file:
    s1 = file.readline()
    s2 = file.readline()

count_ti = 0
count_tv = 0

for i, j in zip(range(len(s1)), range(len(s2))):
    if (s1[i].upper() == "A" and s2[j].upper() == "G") or \
            (s1[i].upper() == "C" and s2[j].upper() == "T") or \
            (s1[i].upper() == "G" and s2[j].upper() == "A") or \
            (s1[i].upper() == "T" and s2[j].upper() == "C"):
        count_ti += 1
    elif s1[i].upper() != s2[j].upper():
        count_tv += 1

print(f"The Transition to Transversion ratio is:\n{round(count_ti / count_tv, 2)}")
