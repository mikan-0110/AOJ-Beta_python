# 3 つの数の整列

# ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。

# Input
# ３つの整数が空白で区切られて与えられます。

# Output
# 小さい順に並べ替えた３つの整数を１行に出力して下さい。整数の間に１つの空白を入れて下さい。

# Constraints
# 1 ≤ ３つの整数 ≤ 10,000



# a, b, c = list(map(int, input().split()))

# if b<c<a:
#     a, b, c = b, c, a
# elif c<a<b:
#     a, b, c = c, a, b
# elif c<b<a:
#     a, b, c = c, b, a
# elif b<a<c:
#     a, b, c = b, a, c
# elif a<c<b:
#     a, b, c = a, c, b
# elif a<b<c:
#     a, b, c = a, b, c

# print(a, b, c)



# x = list(map(int, input().split()))
# x.sort()

# for y in x:
#     print(y,end=' ')



x = list(map(int, input().split()))
x.sort()

print(x[0], x[1], x[2])

