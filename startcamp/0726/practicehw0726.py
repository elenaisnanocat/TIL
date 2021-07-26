#hw
# 1 모음 몇개? .count() 메서드 사용
def count_vowels(word):
    list=['a','e','i','o','u']
    answer=0
    for i in word:
        if i in list:
            answer+=1
    return answer

print(count_vowels('apple'))
print(count_vowels('banana'))




# 3 정사각형만 만들기 

only_square_area = [32, 55, 63], [13, 32, 40, 55]

squre = []
for i in only_square_area[0]:
    for j in only_square_area[1]:
        if i == j:
            squre.append(i * j)
    
print(squre)

# ----------------------------------------------------------------

#wsp


# 1. 과목명-key 점수-value 딕셔너리, 전체 과목 평균점수 반환하는 함수

def get_dict_avg(study):
    study_sum=0
    for i in study.values():
        study_sum+=i
    print(study_sum/len(study))
    # print(sum([i for i in study.values()])/len(study))    

get_dict_avg({'python':80,
'algorithm':90,
'django':89,
'web':83})

# 2.키-혈액형 밸류-사람수 딕셔너리, 혈액형 분류하는 함수

def count_blood(blood):
    blood_list={'A':0,'B':0,'O':0,'AB':0}
    for i in blood:
        if i=='A':
            blood_list['A']+=1
        elif i=='B':
            blood_list['B']+=1
        elif i=='O':
            blood_list['O']+=1
        elif i=='AB':
            blood_list['AB']+=1
    print(blood_list)

count_blood(['A','B','A','O','AB','AB','O','A','B','O','B','AB'])
