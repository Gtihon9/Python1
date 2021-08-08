arr = [[20,1,1,2,2,3,3,5,5,4,20,4,5]


def find_it(seq):
    _dict = {}
    temp = 0
    for i in arr:
        for j in arr:
            if i == j:
                temp += 1
        if temp % 2 != 0:
            return i

print(find_it(arr))
