# print(list(range(1,51)[0:51:2]))


# information = {
#     '강태':'27',
#     '김길':'29',
#     '김혜':'26',
#     '박승':'26',
#     '박유':'29',
#     '박준':'28',
#     '박지':'27',
#     '서상':'29',
#     '우동':'29',
#     '우상':'29',
#     '육현':'28',
#     '윤재':'28',
#     '윤혜':'24',
#     '이명':'25',
#     '이수':'27',
#     '이재':'27',
#     '이종':'29',
#     '이찬':'26',
#     '임혜':'25',
#     '장세':'25',
#     '정인':'28',
#     '홍지':'28'
# }

# print(information.keys())
# print(information.items())




# n=5
# m=9
# for i in range(m):
#     for j in range(n):
#         print("*", end="")
#     print()





# temp = 36.5
# if temp >= 37.5:
#     print('입실 불가')
# else:
#     print('입실 가능')


# result = '입실 불가' if temp >= 37.5 else '입실 가능'
# print(result)

# scores = [80, 89, 99, 83]

# print()

# print((80+89+99+83)/4)


# scores=[80,89,99,83]
# answer=0
# for i in  scores:
#     answer+=i
# print(answer/len(scores))





# ----------------------------------------------------------------------

# sort() 그냥 오름차순
# sort(reverse=True) 내림차순
# 변수 = sorted([]):해당리스트를 오름차순 정렬해줌


# numbers = list(range(1,1001))

# n = int(input("n: "))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i,end=" ")




# N=10
# answers=[]
# for i in range(1,int(N**0.5)):
#     if N%i==0:
#         answers.append(i)
#         answers.append(int(N/i))
# answers.sort()
# print(answers)








# 3.
# number = int(input())

# for i in range(1, number+1):
#     for j in range(1, i+1):
#         print(f'{j}',end = '')
#     print()



