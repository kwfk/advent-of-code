import os

inputs = [int(line.strip()) for line in open('2020/day10/input.txt', 'r')]

inputs.sort()
inputs.insert(0, 0)
inputs.append(inputs[-1] + 3)
print(inputs)

diffs = {}
for i in range(len(inputs) - 1):
    d = inputs[i + 1] - inputs[i]
    if d in diffs:
        diffs[d] += 1
    else:
        diffs[d] = 1
print(diffs[1] * diffs[3])

dp = [0] * len(inputs)
dp[0] = 1
for i in range(1, len(inputs)):
    j = i - 1
    t = 0
    while inputs[i] - inputs[j] <= 3 and j >= 0:
        t += dp[j]
        j -= 1
    dp[i] = t
print(dp[-1])
