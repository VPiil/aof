with open("d4.txt") as f:
    kartta = [list(rivi.strip()) for rivi in f]

rows = len(kartta)
cols = len(kartta[0])
laskuri = 0

# Directions for all 8 neighbors (dx, dy)
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for i, row in enumerate(kartta):
    for j, item in enumerate(row):
        if item == '@':
            paperita = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    if kartta[ni][nj] == '@':
                        paperita += 1
            if paperita < 4:
                laskuri += 1

print(laskuri)
