import string

def clean(line):
    i = 0
    box = list(line)
    
    while i < len(box) - 1:
        if box[i].lower() == box[i + 1].lower():
            if box[i] != box[i + 1]:
                del box[i:i + 2]
                i -= 2
                if i < 0:
                    i = 0
            else:
                i += 1
        else:
            i += 1
    return box

def reduce(line):
    best = ['', len(line)]
    abc = string.ascii_lowercase
    for i in abc:
        s = line.replace(i, "")
        s = s.replace(i.upper(), "")
        c = clean(s)
        print(len(c))
        if len(c) < best[1]:
            best = [i, len(c)]
    print(best)



with open('input.txt', 'r') as fh:
    line = fh.read()
    # s = clean(line)
    # #print(s)
    # print(''.join(s))
    # print(len(s))
    reduce(line)
