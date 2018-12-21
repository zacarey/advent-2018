# Part I
def checksum():
    with open('data.txt') as f:
        two = 0
        three = 0
        line = f.readline()
        while line:
            d = {}
            a = False
            b = False
            for i in line:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            
            for k, v in d.items():
                if v == 2 and not a:
                    two += 1
                    a = True
                if v == 3 and not b:
                    three += 1
                    b = True
            line = f.readline()
        print('Checksum: ' + str(two*three))


# Part II
def find():
    with open('data.txt') as f:
        line = f.readline()
        data = []
        while line:
            data.append(line.replace('\n', ''))
            line = f.readline()
        while data:
            a = data.pop()
            for b in data:
                cur = 0
                count = 0
                idx_bad_char = 0
                for i in b:
                    if i != a[cur]:
                        count += 1
                        idx_bad_char = cur
                    if count > 1:
                        break
                    cur += 1
                if count == 1:
                        print('a: ' + a)
                        print('b: ' + b)
                        print(a[:idx_bad_char] + a[idx_bad_char + 1:])
                        return

find()