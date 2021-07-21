# 1.
# Immutable : String, Tuble, Range
# Mutable : List, Set, Dictionary

# 2.홀수만 담기
# range와 slicing 1~50

# numbers = list(range(1,51))
# odd = numbers[0:-1:2] 
# #1부터 시작해서 끝까지가 0:-1 혹은 ::
# print(odd)

# 4.반복문으로 네모출력
# n = 5
# m = 9
# # for i in range(5):
# #     print(i)
# #     for j in range(5):
# #         print(f'>{j}', end='')
# #     print('')
# #print('')하면 빈문자열을 출력

# n = 5
# m = 9

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print('')

# 5.
# print(입실x) if temp>=37.5 else print(입실o)

# 6.
# scores = [80,89,99,83]
# total = 0
# count = 0
# for score in scores:
#     total += score
#     count += 1

# avg = total/count
# print(avg)


# workshop

# 1.간단한 N의 약수

# user_input = int(input())

# for i in range(1, user_input+1):
#    if user_input % 1 == 0:
#        print(i, end=' ')

# 이거오류남

# 2.중간값 찾기

# numbers = [
#     85,72,
# ]
# length = 0
# for num in numbers:
#     length += 1

# center = length // 2
# sort_list = sorted(numbers)
# print(sort_list[center])

# 다른 풀이방법

# while len(numbers) > 1:
#     numbers.remove(max(numbers))
#     numbers.remove(min(numbers))
# print(numbers[0])

# 3.
# user_input = int(input())

# for i in range(user_input):
#     for j in range(1, i+2):
#         print(f'{j}', end='')
#     print('')
#터미널에 값입력해야함..


# 다른 방법
# num = int(input(''))
# cnt = ""
# for i in range(1,num+1):
#     cnt += str(i) + " "
#     print(cnt)

