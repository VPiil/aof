lines = open("d7.txt").readlines()

drop_id = [0] * len(lines[0])

drop_id[lines[0].index("S")] = 1
counter = 0

for line in lines:
    line = line.strip()
    lineList = list(line)
    for i in range(len(lineList)):
        if lineList[i] != "^" and drop_id[i] == 1:
            lineList[i] = "|"
        if lineList[i] == "^" and drop_id[i] == 1:
            counter += 1
            lineList[i+1] = "|"
            lineList[i-1] = "|"
            drop_id[i+1] = 1
            drop_id[i-1] = 1
            drop_id[i] = 0



    line = "".join(lineList)
    print(line)

print(counter)

    