tiedosto = open("d2.txt").readline()

idt = tiedosto.split(",")

invalids = []

def checkparttwo(l):
    index = 0

    valmis = False

    while not valmis:
        if len(str(l)) % 2 == 0 and index == ( len(l) // 2 ):
             valmis = True
             continue
        
        if len(str(l)) % 2 != 0 and index > round( len(l) // 3 ):
            valmis = True
            continue

        index += 1

        pattern = i[0:index]
        esiintyminen = i.count(pattern)

        if len(i) == esiintyminen * len(pattern):
            invalids.append(i)
            valmis = True
             
    


for id in idt:
    alarange = id.split("-")[0]
    ylarange = id.split("-")[1]
    ranges = [int(alarange), int(ylarange)]

    alakoko = len(alarange)
    ylakoko = len(ylarange)

    for i in range(ranges[0],ranges[1] + 1):
#       work with unmatched numbers only          
            i = str(i)
            if len(i) % 2 == 0:
                first_half = i[:len(i)//2]
                second_half = i[len(i)//2:]

                if first_half == second_half:
                    invalids.append(i)
                
                #checkparttwo(i)

     
    

summa = 0
for luku in invalids:
    summa += int(luku)

print(summa)
