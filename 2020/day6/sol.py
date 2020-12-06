fs = open('2020/day6/input.txt', 'r')

count = 0

line = fs.readline().strip('\n')
while line:
    first = True
    match = set()
    while line:
        check = set()
        for i in list(line):
            check.add(i)
        
        if first:
            match = check
            first = False
        else:
            match = match & check

        line = fs.readline().strip('\n')
    count += len(match)
    print(match)

    line = fs.readline().strip('\n')

print(count)

fs.close()
