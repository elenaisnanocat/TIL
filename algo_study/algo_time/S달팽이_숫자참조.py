T = int(input())
for tc in range(T):
    N = int(input())
    max_n = N * N
    cnt = 1
    idx_x = 0
    idx_y = 1
    idx_d = 0
    dalpang_lst = [[-1 for _ in range(N + 2)] for _ in range( N + 2)]
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            dalpang_lst[y][x] = 0
    dir_x = [1, 0, -1, 0]  #이부분은 되도록 반복문 밖에 젤 바깥에 해주는게 좋다
    dir_y = [0, 1, 0, -1]
    while cnt <= max_n:
        idx_x += dir_x[idx_d]
        idx_y += dir_y[idx_d]
        if dalpang_lst[idx_y][idx_x] == 0:
            dalpang_lst[idx_y][idx_x] = cnt
            cnt += 1
        else:
            idx_x -= dir_x[idx_d]
            idx_y -= dir_y[idx_d]
            idx_d = (idx_d + 1) % 4 #0123이 반복된다 어떤 수를 4로 나눈 나머지는 항상 4보다 작은 정수이다.
    print('#{}'.format(tc+1))
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(dalpang_lst[i][j], end=' ')
        print('')

        # 2345 반복이 필요하면 
        # i in range(100):
        # print( i % 4 + 2)



T = int(input())
 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
for t in range(1, T+1):
    n = int(input())
 
    lst = [[0 for _ in range(n+2)] for _ in range(n+2)]
 
    for i in range(n+2):
        lst[0][i] = -1
        lst[n + 1][i] = -1
        lst[i][0] = -1
        lst[i][n + 1] = -1
 
    i = 1
    j = 0
    num = 1
    d = 0
    while num <= n*n:
        next_i = i + di[d]
        next_j = j + dj[d]
 
        if lst[next_i][next_j]:
            d = (d + 1) % 4
            continue
 
        i = next_i
        j = next_j
        lst[i][j] = num
        num += 1
 
    print('#{}'.format(t))
    for i in range(1, n+1):
        print(*lst[i][1:n+1], sep=' ')