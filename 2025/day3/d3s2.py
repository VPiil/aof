lines = open("d3.txt").readlines()

digits = []

for line in lines:
    digit = ""
    line = line.strip()
    nums = list(map(int, line))
    nNums = []

    start = 0
    end = len(nums) - 11
    
    while len(nNums) != 12:
        index = start
        high = 0
        for n in nums[start:end + len(nNums)]:
            if n > high:
                high = n
                start = index + 1
            index += 1
        nNums.append(high)

    for l in nNums:
        digit += str(l)

    print(str(digit))
    digits.append(digit)

sum = 0
for k in digits:
    sum += int(k)

print("Sum of all digits: ", sum)