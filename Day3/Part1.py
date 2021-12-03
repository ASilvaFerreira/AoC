import time

start_time = time.time()

f = open("input.txt")

sums = [0]*12
gamma = str()
epsilon = str()

for i in f:
    val = i.strip()
    s = 0
    for digit in val:
        if digit == "1":
            sums[s] += 1
        s += 1

for j in sums:
    gamma = gamma + "1" if j > 500 else gamma + "0"
    epsilon = epsilon + "0" if j > 500 else epsilon + "1"

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print(gamma*epsilon)
print("--- %s seconds ---" % (time.time() - start_time))