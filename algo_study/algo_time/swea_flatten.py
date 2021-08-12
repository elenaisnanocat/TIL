T=10
for t in range(T):
    N=int(input())
    #입력값을 int로 받으면서 list로 만들어 준다.
    num=list(map(int, input().split()))
    for i in range(N):
        num.sort()
        num[0]+=1
        num[len(num)-1]-=1
    num.sort()
    print(f"#{t+1} {num[len(num)-1]-num[0]}")