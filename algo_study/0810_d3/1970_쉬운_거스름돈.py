T=int(input())
#존재하는 거스름돈을 배열로 만들어줌
arr=[50000,10000,5000,1000,500,100,50,10]
for t in range(T):
    N=int(input())
    #답을 담아줄 배열
    answer=[]
    for i in arr:
        temp=0
        #줘야할 거스름돈이 잔돈 크기보다 크면 작아질때까지 빼주고
        while N>=i:
            N-=i
            temp+=1
        #temp 결과값을 answer에 넣어준다.
        answer.append(temp)
    print(f"#{t+1}")
    #배열을 1열로 출력하기
    for i in answer:
        print(i, end=" ")
    print()