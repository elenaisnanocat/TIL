T=int(input())
for t in range(T):
    N=int(input())
    #더하기 뺴기를 확인해줄 check
    check=0
    answer=0
    for i in range(1,N+1):
        #check가 0이면 답에 더해주고 (홀수)
        if check==0:
            answer+=i
            check=1
        #1이면 answer에서 빼준다. (짝수)
        elif check==1:
            answer-=i
            check=0
    print(f"#{t+1} {answer}")