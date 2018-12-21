# Part 1
with open("data.txt") as f:
    line = f.readline().replace('""', '')
    n = 0
    while line:
        n += int(line)
        line = f.readline().replace('""', '')
    print('Total: ' + str(n))
        

# Part II
frequency = {0}
frequent = None
n = 0

counter = 0

while not frequent:
    with open("data.txt") as f:
        line = f.readline().replace('""', '')
        while line and not frequent:
            n += int(line)
            if n in frequency:
                frequent = n
                break
            frequency.add(n)
            line = f.readline().replace('""', '')
        counter += 1
print(frequent)
print(counter)

# Works, just is really slow
frequencyList = []
frequentList = None
n = 0
s = counter
counter = 0

while not frequentList:
    with open("data.txt") as f:
        line = f.readline().replace('""', '')
        while line and not frequentList:
            n += int(line)
            if n in frequencyList:
                frequentList = n
                break
            frequencyList.append(n)
            line = f.readline().replace('""', '')
        counter += 1
print(frequentList)