t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print('Case #'+str(i+1)+':',x,'+',y,'=',x+y)
    #str() 정수/실수를 문자열 형태로 앞의 case는 문자열이기에
    #문자열+정수가 나오는 것은 에러 -> 정수를 문자열로 바꿔주기
