tiedosto = open("d1.txt").readlines()

laskuri = 0
suunta = 50

for rivi in tiedosto:
    plus = rivi[0] == "R"
    numero = int(rivi[1:].strip())

    laskuri += (numero//100)
    ylijaama = numero % 100

    if plus:
        ohitukset = (suunta + numero) // 100
        suunta = (suunta + numero) % 100

    else:
        kaannettySuunta = (100 - suunta) % 100
        ohitukset = (kaannettySuunta + numero) // 100
        suunta = (suunta - numero) % 100

    laskuri += ohitukset

print(laskuri)