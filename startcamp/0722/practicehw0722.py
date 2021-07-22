
# wsp

# 1.

# 1)정수 list를 전달 
# 2)각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성.
# 단, list는 65이상 90이하 and 97이상 122이하의 정수로만 구성.

def get_secret_word(list):
    answer=""
    for i in list:
        answer+=chr(i)
    
    return answer


print(get_secret_word([83,115,65,102,89]))


# ###chr()은 괄호안에 있는 숫자를 아스키코드문자로 변환해주는 메서드임
# ###ord()는 괄호안에 있는 문자를 아스키코드로 인식해서 숫자로 변환해주는거


# 2.

# 1)문자열을 전달 받아

# 2) 해당 문자열의 각 문자에 대응되는 아스키 숫자 합을 반환하는
# get_secret_number 함수를 작성. 
# (문자열은 A~Z, a~z로만 구성.)


def get_secret_number(name):
    answer=0
    for i in range(len(name)):
#     #tom이 3글자라서 for i in range(3)과 같음 그래서 0 1 2출력 
        answer+=ord(name[i])
#         #윗줄 받고 name[0],name[1],name[2] 의 ord 값을 다 더함 = t + o + m
    return answer



print(get_secret_number("tom"))


# 3.

# 1)문자열 2개를 전달 받아서
# 2)두 문자열의 각 문자에 대응되는 아스키 숫자들의 합 구함
# 3) 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수 작성

# 방법1)

def get_strong_word(a,b):
#     #'z','tom' 두개는 a ,'a','john' 두개는 b

    num_a=0
    num_b=0
    for i in range(len(a)):
        num_a+=ord(a[i])
#         #이 경우 a = 'tom' 고로 for i in range(3) 
#         #즉 336

    for i in range(len(b)):
        num_b+=ord(b[i])

#         #위랑 동일한 방식으로 여기까지 b값 구하고 
    if num_a>num_b:
        return a
    return b
#         #여기서 두개 각각 합한 값 중 더 큰것 반환.

print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))

# 방법2)

def get_strong_word(a,b):

    if sum([ord(a[i])for i in range(len(a))])>sum([ord(b[i])for i in range(len(b))]):
        return a
    return b
print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))

# 방법3

def get_strong_word(a,b):

    return a if sum([ord(i)for i in a])>sum([ord(i)for i in b]) else b

print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))
