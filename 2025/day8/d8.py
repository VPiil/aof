import math
import os
print("Current working directory:", os.getcwd())

lines = open("d8.txt").readlines()

points = []

for line in lines:
    x, y, z = map(int, line.strip().split(","))
    points.append((x, y, z))

distances = []

for i in range(len(points)):
    x1, y1, z1 = points[i]
    for j in range(len(lines)):
        x2, y2, z2 = points[j]

        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    distances.append(distance)

distances.sort(reverse=True)
no1, no2, no3 = distances[:3]
print(no1)
print(no2)
print(no3)

ans = no1 * no2 * no3

print(ans)
