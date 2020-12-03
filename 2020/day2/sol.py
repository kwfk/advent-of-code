fs = open('2020/day2/input.txt', 'r')

count = 0

while True:
    line = fs.readline()
    if not line:
        break

    args = line.split(' ')
    cond = args[0].split('-')
    letter = args[1][0]
    password = args[2]
    
    # check = password.count(letter)
    # if check <= int(cond[1]) and check >= int(cond[0]):
    #     count += 1

    one = password[int(cond[0]) - 1] == letter
    two = password[int(cond[1]) - 1] == letter
    if one ^ two:
        count += 1

print(count)

fs.close()