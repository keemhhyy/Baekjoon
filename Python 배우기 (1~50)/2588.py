a = int(input())
b = input()

# c=a*int(b[2])
# d=a*int(b[1])
# e=a*int(b[0])
# #그냥 b[]하면 b[]의 숫자가 a만큼 나옴
# print(c)
# print(d)
# print(e)
# print(c+d*10+e*100)

for i in range(3,0,-1):
    print(a*int(b[i-1])) #b[2],b[1],b[0]

print(a*int(b))
          

