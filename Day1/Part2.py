import time

# ADVENT OF CODE DAY 1 - PART1 #

#---------------- MAIN ----------------#

def main(file):
    input = open(file)

    list_input = list()

    for line in input:
        list_input.append(int(line))

    counter = 0

    for i in range(len(list_input)-3):

        if list_input[i] < list_input[i+3]:
            counter +=1

    print("answer is: ", counter)

#---------------- RUN CODE ----------------#

start_time = time.time()

main("inputP1")

print("--- %s seconds ---" % (time.time() - start_time))
