import time
# ADVENT OF CODE DAY 1 - PART1

def main(file):
    input = open(file)
    H = 0
    D = 0
    A = 0

    for line in input:
        command = line.strip()

        if command[0] == "f":
            H += int(command[-1])
            D += A * int(command[-1])
        else:
            A += int(command[-1]) if command[0] == "d" else -int(command[-1])

    result = D * H
    print("answer is: ", result)

start_time = time.time()

main("input.txt")

print("--- %s seconds ---" % (time.time() - start_time))