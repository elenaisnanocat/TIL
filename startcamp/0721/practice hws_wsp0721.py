# hws
# def get_middle_char(char):
#     length = 0
#     for c in char:
#         print(c)
#         length += 1
        
# get_middle_char('ss')
# '될거같은데 안되네...'



# 2
# def get_meddle_char(char):
#     answer=""
#     if len(char)%2==0:
#         for c in range(len(char)//2-1,len(char)//2+1):
#             answer+=char[c]
#     else:
#         answer=char[len(char)//2]
    
#     return answer

# print(get_meddle_char('ss'))
# print(get_meddle_char('coding'))






# 3.
# def fy(name, location='서울'):
#     print(f'{name}의 지역은 {location}입니다.')

# fy('허준')

# fy(location='대전' , name='철수')

# fy('영희', location='광주')

# fy(name='길동', '구미')

# 4.
# def my_func(a, b):
#     c = a + b
#     print(c)

# result = my_func(3, 7)

# 5. 
# def my_avg(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     avg =sum/len(args)
#     print(avg)

# my_avg(77,83,95,80,70)

# ---------------------------------
# wsp

# def list_sum(args):
#     ret = 0
#     for n in range(1, args+1):
#         ret += n
#     return ret
#     print(*args)

# list_sum([1, 2, 3, 4, 5])
# '될거같은데 안됨 왜때문이지'




# 1.
# def list_sum(list):
#     answer=0
#     for i in list:
#         answer+=i
#     return answer


# print(list_sum([1,2,3,4,5]))
