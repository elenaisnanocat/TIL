#테스트 케이스 입력
T=int(input())

#에라토스테네스의 채의 방식을 활용
list = [0 for i in range(1000001)]
#0인경우 소수, 1이면 소수가 아닌 수
list[0]=1
list[1]=1
# 입력되는 최대값까지 미리 소수를 파악하기
for i in range(1000001):
    # list[i]==0, 소수가 아니면
    if list[i]==0:
        #temp에 현재값을 담아두고
        temp=i
        # for문을 돌면서 temp*j는 소수가 아니므로 1을 넣어준다.
        for j in range(2,1000001):
            # 최대값을 넘으면 종료
            if temp * j > 1000000:
                break
            list[temp * j]=1

for t in range(T):
    #입력을 받고
    D, A, B = map(int,input().split())
    answer=0
    #A~B까지 돌면서
    for i in range(A,B+1):
        # list[i]가 0이면 소수를 의미
        #str(i) 숫자를 문자로 바꿔서 str(D)라는 문자가 있으면
        #answer에 1씩 더해준다.
        if list[i]==0 and str(D) in str(i) :
            answer+=1
    # 출력
    print(f"#{t+1} {answer}")