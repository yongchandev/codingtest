a = sorted(list(map(int, input().split())))
while a[0]:
    if a[0]**2 + a[1]**2 == a[2]**2:
        print('right')
    else:
        print('wrong')

    a = sorted(list(map(int, input().split())))
    