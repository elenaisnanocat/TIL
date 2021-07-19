#각 단계에 변수 초기화 하지 않아 오류 발생할 수 있음

#실수비교

a = 0.1 * 3
b = 0.3

import sys
print(abs(a - b) <= sys.float_info.epsilon)
print(sys.float_info.epsilon)

import math
print(math.isclose(a, b))

# string Interpolation
name = '철수야'
print('안녕, %s' % name)

print('안녕, {}'.format(name))

#형 변환 오류발생 #5
print(str(1))
print(int('30'))
print(5)
print(bool('50'))
print(int('3.5'))

#이스케이프 시퀀스 응용
print('"파일은 c:\\Windows\\User\\내문서\\Python에 저장이 되어있습니다." \n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')

#네모 출력

n = 5
m = 9
print(("*"* n + '\n') *m)


#근의 공식
print(-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)



a=3
b=4
c=-7

R1= (-b + (b**2-4*a*c)**0.5)/(2*a)
R2 = (-b - (b**2-4*a*c)**0.5)/(2*a)

print('해는 : ',R1 ,' 또는 ',R2)


#세로로 출력하기 (반복문)
#for i in range(n,m)
#n부터 m-1까지 출력됨
#break 반복문을 종료

i = 10
for i in range(1,11):
    if i == 11:
        break
    print(i)
    i += 1

#거꾸로 세로로 출력하기 (반복문)
#for i in range(n,m,s)
#n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스

n = 5
for i in range(n, 0, -1):
    print(i)


#N줄 덧셈

n = 10
answer = 0 
for i in range(n+1):
    answer += i
print(answer)