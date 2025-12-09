rivit = open("d5.txt").read().strip().splitlines()

ranges = []
for rivi in rivit:
    if "-" in rivi:
        start, end = map(int, rivi.split("-"))
        ranges.append((start, end))

# Sort by starting point
ranges.sort()

# Merge ranges
merged = []
curr_start, curr_end = ranges[0]

for start, end in ranges[1:]:
    if start <= curr_end + 1:  # overlapping or adjacent
        curr_end = max(curr_end, end)
    else:
        merged.append((curr_start, curr_end))
        curr_start, curr_end = start, end

merged.append((curr_start, curr_end))

# Compute total coverage length
laskuri = sum(end - start + 1 for start, end in merged)

print(laskuri)
