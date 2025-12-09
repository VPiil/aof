rivit = open("d3.txt").readlines()

luvut = []

for rivi in rivit:
    rivi = rivi.strip()
    listana = list(map(int, rivi))
    suurin = max(listana[:len(listana)-1])

    index = listana.index(suurin)
    
    toiseksisuurin = max(listana[index+1:])

    luku = str(suurin) + str(toiseksisuurin)
    print(luku)
    luvut.append(luku)

summa = 0
for nro in luvut:
    summa += int(nro)

print("lukujen summa on: ", summa)