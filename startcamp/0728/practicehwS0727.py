# 1. sorted([]) 원본 변환 x 반환 o 
#   [].sort()  원본 변환o 반환x

# 2. a =[]
# a.append('abc')  -> ['abc'] 리스트 마지막에 인자를 추가
# a.extend('abc')  -> ['a','b',c] 인자의 요소를 더해줌

# 3. 복사가 잘 된건가?
# 1차원 복사 shallow copy 1.슬라이싱 2.list() 3.copy.copy

# 2차원이상 복사 deepcopy 1.copy.deepcopy

# wsp

# 1.무엇이 중복일까

def duplicated_letters(word):
    result = []
    for char in word:
        #1. and 이후 조건문으로 리스트에 중복되는 값이 들어가지 않도록 하는 방법
        if word.count(char) > 1 and char not in result :
            result.append(char)

    return result
    # result =list(set(result))) 2.set으로 리스트 중복 제거하는 방법

res1 = duplicated_letters('apple')
res2 =duplicated_letters('banana')

print(res1)
print(res2)

2.

def low_and_up(word):
# 방법1 for 문 사용
    # length = len(word)
    # result = ''
    # for idx in range(length):
    #     if idx % 2 : #odd(홀수)
    #         result += word[idx].upper()
    #     else:
    #         result += word[idx].lower()
    # return result

# 방법2 리스트 컴프리헨션 + 조건표현식
#     result = [char.upper() if idx % 2 else char.lower() for idx, char in enumerate(word)]

#     return ''.join((result))


# res1 = low_and_up('apple')
# res2 = low_and_up('banana')
# print(res1)
# print(res2)


# 3.
# 방법1
# def lonely(numbers):
#     result = [numbers[0]]
#     for num in numbers:
#         if result[-1] != num:
#             result.append(num)

# 방법2
    # result = []
#     for idx, num in enumerate(numbers):
#         if idx == 0:
#             result.append(num)

#         elif result[-1] != num:
#             result.append(num)

#     return result




# res1 = lonely([1,1,3,3,0,1,1])
# res2 = lonely([4,4,4,3,3])
# print(res1)
# print(res2)