def Solution1():
    count_in_shop= {'XS':[0, 1000], 'S':[0, 1001], 'M':[0, 1002], 'L':[0, 1003], 'XL': [0,1004]}
    count_request = {'XS':[0, 1000], 'S':[0, 1001], 'M':[0, 1002], 'L':[0, 1003], 'XL': [0,1004]}
    while True:
        num_in_shop = input('number of in shop: ')
        size_in_shop = input('size: ').split()
        if size_in_shop != len(num_in_shop):
            print('number of T is not eqaul to your input, pleaze re-input')
            continue
        else:
            break

    for i in size_in_shop:
        if i not in count_in_shop():
            X_count = i.count('X')
            count_in_shop[i] = [1, X_count - 1]
        count_in_shop[i][0] += 1

    while True:
        num_request = input('number of request: ')
        size_request = input('size of request: ').split()
        if num_request != len(size_request):
            print('number of T is not eqaul to your input, pleaze re-input')
            continue
        else:
            break
    
    