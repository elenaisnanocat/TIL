T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst_n = [list(map(int, input().split())) for _ in range(N)]
 
 
    max_result = 0
    
    for r in range(N-M+1):
        for c in range(N-M+1):
            kill_num = 0
            row = r
            col = c
            for m in range(M): 
                kill_num += sum(lst_n[row+m][col:col+M])
            if max_result < kill_num:
                max_result = kill_num
 
    print('#{} {}'.format(tc, max_result))




for t in range(int(input())):
    M, N = map(int,input().split())
    lst = []
    for i in range(M):
        lst.append(list(map(int,input().split())))
    total = 0
    result = 0
    for y in range(M-N+1):
        for x in range(M-N+1):
            for i in range(N):
                for j in range(N):
                    total += lst[y+i][x+j]
            result = max(result,total)
            total=0
    print(f'#{t+1} {result}')