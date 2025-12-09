rivit = open("d5.txt").readlines()

ranges = []
nums = []

for rivi in rivit:
    rivi = rivi.strip()
    if "-" in rivi:
        ranges.append(rivi)
    elif rivi.isdigit():
        nums.append(int(rivi))

rajat = []
for raj in ranges:
    start, end = raj.split("-")
    rajat.append(range(int(start), int(end) + 1))


laskuri = 0

for num in nums:
    print(num)
    for raja in rajat:
        if num in raja:
            laskuri += 1
            break

print(laskuri)

