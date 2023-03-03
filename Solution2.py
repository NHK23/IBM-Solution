def Solution2():
    result = []
    count = 0
    num = int(input('Number: '))
    while count < num:
        temp = input('Input:')
        result.append(temp.split())
        count += 1
    check(result)
    
def check(result):
    count = 0
    temp_list = []
    for i in range(len(result)):
        if result[i][1] == 'false':
            count += 1
            temp_list.append(result[i][2])
    if count != 0:
        print('No', str(temp_list))

Solution2()