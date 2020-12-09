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

def part2():
    start = 0
    end = 1
    tmp = 0
    for i in range(len(nums)):
        curr = nums[i]
        j = i + 1
        while True:
            if curr == special:
                return min(nums[i:j]) + max(nums[i:j])
            if curr > special or j == len(nums):
                break
            curr += nums[j]
            j += 1

print(part2())



# found = False
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         target = nums[i:j]
#         if sum(target) == special:
#             mini = min(target)
#             maxi = max(target)
#             print(mini + maxi)
#             found = True
#             break
#     if found:
#         break

fs.close()
