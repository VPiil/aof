lines = open("d9.txt").readlines()

coordinates = []

for line in lines:
    line = line.strip()
    parts = line.split(",")
    x, y = map(int, parts)
    coordinates.append((x, y))
    print(line)

biggest = 0

for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i == j:
            continue
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]

        xdif = abs(x1 - x2) + 1 ## + 1 because array stars 0...
        ydif = abs(y1 - y2) + 1

        area = xdif * ydif

        if area > biggest:
            biggest = area
print(f"Biggest area we can do of coordinates is {biggest}")