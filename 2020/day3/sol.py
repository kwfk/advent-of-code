fs = open('2020/day3/input.txt', 'r')

first = fs.readline()

slope1, slope1Pos, slope1Count = 1, 1, 0
slope2, slope2Pos, slope2Count = 3, 3, 0
slope3, slope3Pos, slope3Count = 5, 5, 0
slope4, slope4Pos, slope4Count = 7, 7, 0
slope5, slope5Pos, slope5Count = 1, 1, 0
lineCount = 1

length = len(first) - 1

while True:
    line = fs.readline().strip('\n')
    if not line:
        break
    
    if line[slope1Pos] == '#':
        slope1Count += 1
    if line[slope2Pos] == '#':
        slope2Count += 1
    if line[slope3Pos] == '#':
        slope3Count += 1
    if line[slope4Pos] == '#':
        slope4Count += 1
    if lineCount % 2 == 0:
        if line[slope5Pos] == '#':
            slope5Count += 1
        slope5Pos = (slope5Pos + slope5) % length


    slope1Pos = (slope1Pos + slope1) % length
    slope2Pos = (slope2Pos + slope2) % length
    slope3Pos = (slope3Pos + slope3) % length
    slope4Pos = (slope4Pos + slope4) % length
    lineCount += 1

print(slope1Count, slope2Count, slope3Count, slope4Count, slope5Count)
print(slope1Count * slope2Count * slope3Count * slope4Count * slope5Count)

fs.close()
