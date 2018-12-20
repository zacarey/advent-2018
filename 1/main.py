frequency = []
frequent = None
n = 0

def addFrequency(i):
    if i in frequency:
        frequent = i
        print(i)
        return i
    frequency.append(i)


while not frequent:
    with open("data.txt") as f:
        line = f.readline().replace('""', '')
        while line:
            n += int(line)
            addFrequency(n)
            line = f.readline().replace('""', '')
print(frequent)

# Part II
