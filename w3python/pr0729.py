# #전역 변수 : 함수 외부에서 생성된 변수, 함수 내부,외부 모두 사용가능
# x = 'awesome'

# def myfunc():
#     print('Python is ' + x)

# myfunc()

#함수 내에서 같은 이름의 변수를 생성하면 이 변수는 지역 변수가 되며 함수 내에서만 사용할 수 있습니다.
# 동일한 이름을 가진 전역 변수는 원래 값으로 전역적으로 유지됩니다.

# x = 'awesome'

# def myfunc():
#     x = 'fantastic'
#     print('Python is ' + x )

# myfunc()

# print('Python is ' + x )

#global 키워드를 사용하는 경우 변수는 전역 범위에 속합니다.

# def myfunc():
#     global x
#     x = 'fantastic'

# myfunc()

# print('Python is ' + x )

# 또한 global 함수 내에서 전역 변수를 변경 하려면 키워드를 사용

# x = 'awesome'

# def myfunc():
#     global x 
#     x = 'fantastic'

# myfunc()

# print('Python is ' + x )

#파이썬 데이터 유형
##내장 데이터 유형
#변수는 다른 유형의 데이터를 저장할 수 있으며 다른 유형은 다른 작업을 수행할 수 있습니다.

#텍스트 유형 : str
#숫자 유형 : int, float, complex
#시퀀스 유형 : list, tuple, range
#매핑 유형 : dict
#세트 유형 : set, frozenset
#부울 유형 : bool
#바이너리 유형 : bytes, bytearray, memoryview

#특정 데이터 유형 설정
#데이터 유형을 지정하려면 다음 생성자 함수를 사용할 수 있다.

# x = 5 
# print(type(x))

# x = str('hello world')
# y = int(20)
# z = float(20.5)
# xy = complex(1j)
# yz = list(('apple', 'banana', 'cherry'))
# xx = tuple(('apple', 'banana', 'cherry'))
# yy = dict(name='john', age = 36)
# zz = set(('apple', 'banana', 'cherry'))

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(xy))
# print(type(yz))
# print(type(xx))
# print(type(yy))
# print(type(zz))

# print(x)
# print(y)
# print(z)
# print(xy)
# print(yz)
# print(xx)
# print(yy)
# print(zz)

#파이썬 숫자
#int
#float
#complex

#난수
#파이썬에는 random() 난수를 만드는 함수가 없지만 파이썬에는 random 난수를 만드는데 사용할 수 있는 내장 모듈이 있다.

#random 모듈을 가져오고 1과 9 사이의 난수를 표시함.
# import random
# print(random.randrange(1,10))

#파이썬 캐스팅
#변수 유형 지정
#변수에 유형을 지정하려는 경우가 있다. 이것은 캐스팅으로 가능. Python은 객체 지향 언어이므로 클래스를 사용하여 기본 유형을 포함한 데이터 유형을 정의함
#파이썬에서의 캐스팅은 생성자 함수를 사용하여 수행.

#int() - 정수 리터럴, 부동 리터럴(모든 소수 제거)또는 문자열 리터럴(문자열이 정수를 나타내도록 제공)에서 정수를 생성
#float() - 정수 리터럴, 부동 리터럴 또는 문자열 리터럴에서 부동 소수점 수를 생성(문자열이 부동 소수점 똔느 정수를 나타내는 경우)
#str() - 문자열, 정수 리터럴 및 부동 리터럴을 포함한 다양한 데이터 유형에서 문자열을 구성합니다.

# x = int(2.8)
# y = float('3')
# z = str(2)

# ---------------------------------------------------------------------------------------------

#파이썬 문자열(String)
#문자열 

#변수에 문자열 할당
#변수에 문자열을 할당하는 것은 변수 이름 뒤에 등호와 문자열을 사용

# a = "hello world"
# print(a)

#문자열은 배열입니다.
#Python의 문자열은 유니코드 문자를 나타내는 바이트 배열입니다.
#그러나 Python에는 문자 데이터 유형이 없으며 단일 문자는 단순히 길이가 1인 문자열입니다.
#대괄호를 사용하여 문자열의 요소에 액세스할 수 있습니다.

#위치 1의 문자 가져오기(첫번째 문자의 위치가 0임)

# a = 'hello world!'
# print(a[1])

#문자열 루핑
#문자열은 배열이므로 루프를 사용하여 