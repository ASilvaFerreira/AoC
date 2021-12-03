import time

start_time = time.time()

f = open("input.txt")

def most_common_bit(data, pos):  # computes the most common bit at position = pos
    mcn = 0 
    for binary in data:
        mcn += 1 if binary[pos] == "1" else 0
    return "1" if mcn >= len(data)/2 else "0"

def least_common_bit(data, pos):  # computes the least common bit at position = pos
    mcn = 0 
    for binary in data:
        mcn += 1 if binary[pos] == "1" else 0
    return "0" if mcn >= len(data)/2 else "1"

def sieve_input(data, tracker, operation=1):
    output = list()
    var = 0
    pos = tracker
    compare_bit = most_common_bit(data, pos) if operation == 1 else least_common_bit(data, pos)

    for binary in data:
        if binary[pos] == compare_bit:
            output.append(binary)
    pos += 1

    if len(output) != 1:
        var = sieve_input(output, pos, operation)
    else:
        var = int(output[0], 2)
        return var
    return var

start_time = time.time()
f = open("input.txt")

reading = list()
for i in f: 
    val = i.strip()
    reading.append(val)

oxygen = sieve_input(reading, 0)
carbon = sieve_input(reading, 0, 0)


print(oxygen, carbon, oxygen * carbon)
print("--- %s seconds ---" % (time.time() - start_time))