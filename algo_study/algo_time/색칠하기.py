

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr=[['']*10 for _ in range(10)]
    #행렬을 돌며 color가 1이면 R color가 2이면 B를 추가
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if color == 1:
                    arr[i][j] += 'Red'
                else:
                    arr[i][j] += 'Blue'
    #행렬을 돌며 R가 B가 모두 있으면 보라색으로 간주하고 cnt += 1
    purple = 0
    for i in range(10):
        for j in range(10):
            if 'Red' in arr[i][j] and 'Blue' in arr[i][j]:
                purple += 1
    print('#{} {}'.format(t,purple))





T = int(input())
for idx in range(1, T + 1):
    N = int(input())
    Map = [[0] * 10 for _ in range(10)]
    count = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if Map[r][c] and Map[r][c] != color:
                    Map[r][c] = 3
                    count += 1
                else:
                    Map[r][c] = color
 
    print(f'#{idx} {count}')