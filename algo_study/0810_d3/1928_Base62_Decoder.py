from base64 import b64decode
 
T = int(input())
 
for t in range(T):
 
    word = input()
    #base64 Encode를 사용을 하면 문자열을 자동으로 변환해준다.
    answer = b64decode(word).decode('UTF-8')
 
    print(f'#{t+1} {answer}')