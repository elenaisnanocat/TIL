T=int(input())
for t in range(T):
    word=input()
    #한 단어의 길이가 10개까지로 제한
    for j in range(1,10):
        #다음 단어와 중복이 되면 결과를 출력
        #j가 2일 경우 word=koreakoreakorea word[:j]=ko, word[j:2*j]=re
        if word[:j]==word[j:2*j]:
            print(f'#{t+1} {j}')
            break