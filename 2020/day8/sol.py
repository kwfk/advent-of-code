fs = open('2020/day8/input.txt', 'r')

instr = []

line = fs.readline().strip('\n')
while line:
    instr.append(line)
    line = fs.readline().strip('\n')


def parse(instruction):
    i, arg = instruction.split(' ')
    if i == 'nop':
        return [0, int(arg)]
    if i == 'acc':
        return [1, int(arg)]
    if i == 'jmp':
        return [2, int(arg)]


def traverse(pos, v, acc, a = []):
    while True:
        if pos in v:
            return (acc, False)
        if pos >= len(instr):
            return (acc, True)
        
        # visited.add(pos)
        v.append(pos)
        ins, arg = parse(instr[pos])

        a.append(acc)
        if ins == 1:
            acc += arg
        elif ins == 2:
            pos += arg
            continue

        pos += 1

visited = []
a = []
print(traverse(0, visited, 0, a))

for i in range(len(visited)):
    ins, arg = parse(instr[visited[i]])

    if ins == 0:
        acc, end = traverse(visited[i] + arg, visited[:i + 1], a[i])
        if end:
            print(acc)
    elif ins == 2:
        acc, end = traverse(visited[i] + 1, visited[:i + 1], a[i])
        if end:
            print(acc)




fs.close()
