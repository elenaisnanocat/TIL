# 1)T=int(input())

# for i in range(T):
#     D, A, B, F =map(int,input().split())
#     time=D/(A+B)
#     print(f"#{i+1} {F*time}")



# 2)T=int(input())

# for i in range(T):
#     D, A, B, F =map(int,input().split())
#     print(f"#{i+1} {F*D/(A+B)}")


#테스트 케이스 수 입력
T=int(input())


for i in range(T):
    #네 정수 입력
    D, A, B, F =map(int,input().split())
    #시간=거리/속력 (기차 A+B) 즉 충돌하는 시간
    time=D/(A+B)
    #시간 * 속력 = 이동거리
    answer=F*time
    #결과 출력
    print(f"#{i+1} {answer}")


