import itertools
import sys

lines = open("d10.txt").readlines()

class Machine:
    def __init__(self):
        self.goal = []
        self.indicators = []
        self.joltages = []

    def createGoal(self, goalstr):
        goal_list = list(goalstr)
        goal_list.remove("[")
        goal_list.remove("]")
        for i in range(len(goal_list)):
            if goal_list[i] == ".":
                goal_list[i] = 0
            elif goal_list[i] == "#":
                goal_list[i] = 1
        self.goal = goal_list
    
    def createIndicators(self, indi_list):
        for block in indi_list:
            clean = block.strip("()")
            block_list = clean.split(",")
            nums = [int(x) for x in block_list]
            self.indicators.append(nums)

    def createJoltages(self, jols):
        clean = jols.strip("{}")
        jList = clean.split(",")
        for x in range(len(jList)):
            self.joltages.append(int(jList[x]))

    def combinations(self):
        combs = []
        stuff = self.indicators
        for k in range(len(stuff) + 1):
            for subset in itertools.combinations(stuff, k):
                combs.append(subset)
        return combs
    
    def createEmpty(self, arr):
        empty = []
        for _ in range(len(arr)):
            empty.append(0)
        return empty

    def configure(self):
        empty_template = self.createEmpty(self.goal)
        combs = self.combinations()
        best = 10
        for comb in combs:
            empty = empty_template.copy()
            for comb_part in comb:
                for h in range(len(comb_part)):
                    num = comb_part[h]
                    if empty[num] == 0:
                        empty[num] = 1
                    else: 
                        empty[num] = 0
            if self.goal == empty:
                if len(comb) < best:
                    best = len(comb)
        return best




#Part 1
counter = 0
for line in lines:
    machine = Machine()
    line = line.strip()
    parts = line.split(" ")
    goall = parts[0]
    indis = []
    for part in parts:
        if "(" in part:
            indis.append(part)
    machine.createGoal(goall)
    machine.createIndicators(indis)
    counter += machine.configure()
    del machine

print(f"Part 1: {counter}")
