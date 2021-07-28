# import random
# number = random.sample(range(1,50),4)
# print(number)

# number.sort()
# print(number)

# print(number.sort(reverse=True))
# print(number)

# import random
# number = random.sample(range(1,50),4)
# print(number, sorted(number))

# x = [1, 2, 3]
# x.append([4, 5])
# print (x)


# x = [1, 2, 3]
# x.extend([4, 5])
# print (x)



# # 3
# # a = [1, 2, 3, 4, 5]
# # b = a

# # a[2] = 5

# # print(a)
# # print(b)


def lonely(num):
    new_list = []
    for i in num:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

lonely([1,1,3,3,0,1,1])
lonely([4,4,4,3,3])