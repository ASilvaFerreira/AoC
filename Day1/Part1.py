import time
# ADVENT OF CODE DAY 1 - PART1

def main(file):
    input = open(file)

    list_input = list()

    for line in input:
        list_input.append(int(line))

    counter = 0

    for i in range(len(list_input)-1):

        if list_input[i+1] > list_input[i]:
            counter +=1

    print("answer is: ", counter)

start_time = time.time()

main("input.txt")

print("--- %s seconds ---" % (time.time() - start_time))

