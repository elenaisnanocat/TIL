# command 매 초 정수
# 0 : 현재 속도 유지.
# 1 : 가속
# 2 : 감속

T = int(input())
for tc in range(1,1+T):
    N = int(input())  # N초 
    C = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    velocity = 0
    for q in C:
        if q[0] == 1:
            velocity += q[1]
        elif q[0] == 2:
            velocity -= q[1]
            if velocity < 0:
                velocity = 0
        ans += velocity          #해당 초당 속도만큼 이동해서 총 이동거리인 ans에 더해준다.
 
    print('#{} {}'.format(tc,ans))