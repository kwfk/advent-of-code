fs = open('2020/day1/input.txt', 'r')
nums = fs.readlines()
for i in range(len(nums) - 1):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            one = int(nums[i])
            two = int(nums[j])
            thr = int(nums[k])
            sum = one + two + thr
            if sum == 2020:
                print(one * two * thr)
fs.close()