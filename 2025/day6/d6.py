rivit = open("d6.txt").readlines()

kartta = []

for rivi in rivit:
    osat = rivi.split()
    if osat[0].isnumeric():
        rivin_nrot = []
        for x in osat:
            rivin_nrot.append(int(x))
        kartta.append(rivin_nrot)
    else:
        operaattorit = osat

total = 0

for i in range(len(kartta[0])):
    luku = 0
    nums = []
    for k in range(len(kartta)):
        nums.append(kartta[k][i])

    if operaattorit[i] == "*":
        luku = 1
        for num in nums:
            luku *= num
    elif operaattorit[i] == "+":
        for num in nums:
            luku += num
    total += luku
print(total)




