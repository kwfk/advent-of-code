fs = open('2020/day5/input.txt', 'r')

hId = 0

ids = []

while True:
    line = fs.readline().strip('\n')
    if not line:
        break

    row = line[:-3]
    col = line[-3:]

    bRow = row.replace('F', '0').replace('B', '1')
    bCol = col.replace('L', '0').replace('R', '1')

    r = int(bRow, 2)
    c = int(bCol, 2)

    id = r * 8 + c

    hId = max(id, hId)
    ids.append(id)

print(hId)

ids.sort()

mid, low, high = 0, 0, len(ids) - 1

while high > low:
    mid = (low + high - 1) // 2
    if ids[mid] - mid == ids[0]:
        if ids[mid + 1] - ids[mid] > 1:
            print(ids[mid] + 1)
            break
        else:
            low = mid + 1
    else:
        if ids[mid] - ids[mid - 1] > 1:
            print(ids[mid] - 1)
            break
        else:
            high = mid - 1

fs.close()
