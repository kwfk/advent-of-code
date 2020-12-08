import re
fs = open('2020/day7/input.txt', 'r')

link = {}
inside = {}

line = fs.readline().strip('\n')
count = 1

def cAndB(bag):
    if bag == 'no other':
        return
    s = bag.split(' ')
    return (' '.join(s[1:]), s[0])

while line:
    bag, contained = line.split(' bags contain ')
    # print(contained.split(' bag'))
    p = re.sub(' bags*', '', contained).strip('.').split(', ')
    s = [re.sub('\d+ *', '', b) for b in p]
    t = [cAndB(b) for b in p]
    inside[bag] = set(t)
    for c in s:
        if c in link:
            link[c].add(bag)
        else:
            link[c] = {bag}

    line = fs.readline().strip('\n')
    count += 1

sg = set()

def search(bag):
    if bag in link:
        for b in link[bag]:
            sg.add(b)
            search(b)

search('shiny gold')
print(len(sg))

def look(bag):
    count = 0
    for b in inside[bag]:
        if b is None:
            count += 0
        else:
            count += int(b[1]) * look(b[0])
    print(bag, count)
    return 1 + count
print(look('shiny gold'))



fs.close()
