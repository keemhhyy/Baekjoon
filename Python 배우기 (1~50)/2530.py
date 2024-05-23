h, m, s = map(int,input().split())
d = int(input()) #초


s += d %60
d = d//60
if s>=60:
    m+=1
    s-=60

m += d%60
d= d//60
if m>=60:
    h+=1
    m-=60

h += d%24 
if h>=24:
    h-=24
    
print(h,m,s)  


# a += (d%60)//60
# b += (d-(d%60))//60
# c += d%60

# if c>=60:
#     b+=1
#     c-=60

# if b>=60:
#     a+=1
#     b-=60

# if a>=24:
#     a-=24

# print(a,b,c)    