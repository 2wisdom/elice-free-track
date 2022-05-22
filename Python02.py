#1. 입력

#변수 = input() : 변수에 입력받은 값을 집어넣겠다는 의미

var = input()


#어떤 것을 입력하든 문자열로 입력되기 때문에 형 변환이 필요
#int() : 정수형 변환, str() : 문자열 변환 등…

var1 = input() #4 입력
var1 = int(var1)
var2 = int(input()) #3 입력
print(3+var1+var2) #10 출력


#2. 논리 자료형(Boolean Data)


#논리 자료형 : 참(True) 혹은 거짓(False)을 나타내는 자료형

True, False


#비교 연산자 : 숫자나 문자의 값을 비교하는 연산자
#주어진 진술이 참이면 True, 거짓이면 False

A == B #A와 B가 같다
A != B #A와 B가 다르다
A >= B #A가 B보다 크거나 같다
A <= B #A가 B보다 작거나 같다
A > B #A가 B보다 크다
A < B #A가 B보다 작다

print(3 == 3) #True
print(3 != 3) #False


#논리 연산자 : 논리 자료형 사이의 연산

AND : 각 논리가 모두 True이면 결과가 True  
OR : 각 논리 중 True가 존재하면 결과가 True  
NOT : 논리값을 뒤집는 연산


#3. 조건문

#조건에 따라 특정 명령을 수행하는 구문

#if문 : 조건이 참이면 명령을 수행

if a >= 5:
    print("a는 5 이상입니다!")


#elif문 : 이전 조건이 거짓인 상황에서 조건이 참이면 명령을 수행

if a >= 5:
    print("a는 5 이상입니다!")
elif a >= 3:
    print("a는 3 이상 5 미만입니다!")


#else문 : 위의 조건에 해당하지 않는 모든 경우에 수행

if a >= 5:
    print("a는 5 이상입니다!")
elif a >= 3:
    print("a는 3 이상 5 미만입니다!")
else:
    print("a는 3 미만입니다!")


#조건문에 들어가는 명령들은 같은 들여쓰기로 구분!
