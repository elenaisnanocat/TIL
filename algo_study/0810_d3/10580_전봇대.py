TC=int(input())
for t in range(TC):
    N=int(input())
    #입력을 받아줄 num 리스트를 선언
    num=list()
    answer=0
    for n in range(N):
        #입력을 받아준다.
        b, c = map(int, input().split())
        #리스트에 넣어준다.
        num.append([b,c])
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            #입력값들의 차이를 비교해 보면서 양쪽이 음수와 양수로 다를 경우 answer에 1을 더해준다.
            if num[i][0]-num[j][0]>=0 and num[i][1]-num[j][1]<0:
                answer+=1
            elif num[i][0]-num[j][0]<0 and num[i][1]-num[j][1]>=0:
                answer+=1

    print(f"#{t+1} {answer}")