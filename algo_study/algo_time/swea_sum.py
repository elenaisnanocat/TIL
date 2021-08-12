for _ in range(10) :
    T = int(input())
    N = 100

    arr = [list(map(int, input().split())) for _ in range(N)]

    side = 0 
    for i in range(N) :
        sum = 0
        for j in range(N) :
            sum += arr[i][j] # 행 합
        if sum > side : 
            side = sum  #동일한 최댓값이 있을 경우, 하나의 값만 출력

    col = 0
    for j in range(N) :
        sum = 0
        for i in range(N) :
            sum += arr[i][j] # 열 합
        if sum > col :
            col = sum  #동일한 최댓값이 있을 경우, 하나의 값만 출력

    cross = 0
    for i in range(N) :
        sum_down = 0
        sum_up = 0
        sum_down += arr[i][i] # 대각선 합 ↘
        sum_up += arr[i][99-i] # 대각선 합 ↙
        cross = max(sum_down, sum_up)

    print("#{} {}".format(T, max(side, col, cross)))