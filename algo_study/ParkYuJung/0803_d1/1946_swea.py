# 1
# 3
# A 10
# B 7
# C 5   

T = int(input())
#숫자입력받기
for t in range(1, T+1): 
    N = int(input())
    doc = ''
    for j in range(N):
        Ci, Ki = input().split() 
        #알파벳 Ci와 알파벳의 연속된 개수 Ki를 .split()으로 공백을 기준으로 나눠준다
        Ki = int(Ki)
        while True:
            if Ki <= 0:
                break
            #알파벳 개수가 0이거나 그보다 작으면 멈춤
            Ki -= 1
            doc += Ci
            #Ki가 1씩 줄때마다 Ci인 알파벳 하나씩 더함


    print('#{}'.format(t))
    count = 1
    for c in doc:
        print(c, end='')
        if count % 10 == 0:
            print()
        count += 1
    print()
 