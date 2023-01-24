x = input()
a, b, c = list(map(int, x.split()))

if a < b < c:
    print("Yes")

else:
    print("No")


#他の人の解答
# a,b,c=map(int,input().split())

# if a<b and b<c:
#     print("Yes")
# else:
#     print("No")
