import time
# ADVENT OF CODE DAY 1 - PART1

def main(file):
    input = open(file)

    
    print("answer is: ")

start_time = time.time()

main("input.txt")

print("--- %s seconds ---" % (time.time() - start_time))
