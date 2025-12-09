rivit = open("d6.txt").readlines()

kartta = []

for rivi in rivit:
    osat = rivi.split(" ")
    if osat[0].isnumeric():
        rivin_nrot = []
        for x in osat:
            rivin_nrot.append(x)
        kartta.append(rivin_nrot)
    else:
        operaattorit = osat

total = 0

for i in range(len(kartta[0])):
    luku = 0
    nums = []
    for k in range(len(kartta)):
        if i < len(kartta[k]):
            nums.append(list(str(kartta[k][i])))
    # p
#   j s1 s2 s3 ...
    # r1 r2 r3 ...
    # g1 g2 g3 ...
    # k1 k2 k3 ...
    newNums = []
    longest = max(nums, key=len)
    for j in range(len(longest)):
        apuS = ""
        for p in range(len(nums)):
            if j < len(nums[p]):
                apuS += str(nums[p][j])
        if apuS.isdigit():
            newNums.append(int(apuS))


    if operaattorit[i] == "*":
        luku = 1
        for num in newNums:
            luku *= num
    elif operaattorit[i] == "+":
        for num in newNums:
            luku += num
    total += luku
print(total)
