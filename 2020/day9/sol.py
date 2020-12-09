fs = open('2020/day9/input.txt', 'r')

preamble = []
nums = []
for i in range(25):
    num = int(fs.readline().strip())
    preamble.append(num)
    nums.append(num)

def checkSum(target):
    check = {}
    for i in range(len(preamble)):
        if target - preamble[i] in check:
            return [check[target - preamble[i]], preamble[i]]
        else:
            check[preamble[i]] = preamble[i]

line = fs.readline().strip()

special = 0
while line:
    num = int(line)
    nums.append(num)

    two = checkSum(num)
    if two is None:
        print(num)
        special = num


    preamble = preamble[1:] + [num]
    line = fs.readline().strip()

found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        target = nums[i:j]
        if sum(target) == special:
            mini = min(target)
            maxi = max(target)
            print(mini + maxi)
            found = True
            break
    if found:
        break

fs.close()
