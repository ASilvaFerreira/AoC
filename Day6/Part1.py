import time
from typing import Generator

start_time = time.time()

input = open("input.txt")
input=list(map(int, input.readline().strip().split(",")))

totalFish = len(input)
totalDays = 390000
GeneratorFish = [0]*totalDays
day = 1

for i in input:
    GeneratorFish[i] += 1

for day in range(totalDays):
    if day < totalDays - 9:
        GeneratorFish[day + 7] += GeneratorFish[day]
        GeneratorFish[day + 9] += GeneratorFish[day]
    elif totalDays - 9 <= day < totalDays - 7:
        GeneratorFish[day + 7] += GeneratorFish[day]
    totalFish += GeneratorFish[day]

print("answer is:", totalFish)
print(time.time()-start_time)