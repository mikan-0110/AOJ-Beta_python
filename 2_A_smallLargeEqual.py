x = input()
a,b = list(map(int, x.split()))

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')