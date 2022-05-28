1. 함수
Point I
특정 기능을 수행하는 코드(들의 모임)
함수이름(인자) 형태로 사용

Point II
내장 함수 : 형식에 맞춰서 편리하게 사용

Point III
max(), min() - 시퀀스의 최댓값, 최솟값을 구하는 함수

print(max([1, 2, 3]))
#3

print(min([-1, -2, -3]))
#-3
Point IV
sum(), len()- 시퀀스의 합과 길이를 구하는 함수

odds = [1, 3, 5, 7, 9, 11]
print(sum(odds))
#36

print(len(odds))
#6
Point V
def 키워드 : 함수를 정의할 때 사용

def function_name():
    ....
Point VI
매개변수 : 함수 외부에서 내부로 값을 전달할 때 사용되는 변수
함수를 정의할 때 괄호 안에 써주는 것

def function(var1, var2, ...):
    ...
Point VII
인자 : 함수 외부에서 내부로 전달한 값(자료)
함수를 사용할 때 괄호 안에 써주는 것

def function(var1, var2):
    #이때 var1, var2는 매개변수
        ...

function(1, 2)
#이때 1, 2은 인자
Point VIII
전역변수 : 어디서든지 사용 가능한 변수
지역변수 : 특정 구문 안에서 정의한 변수

x = 1 #전역변수
def func():
    x = 2 #지역변수
    print(x)
Tip!
print() 함수의 형식

print(data, end="\n", sep=" ")
data에는 출력할 자료를, end에는 data 출력 이후 출력할 문자열을 넣습니다. (기본값은 줄바꿈 문자 "\n"입니다.)

sep에는 data가 여러개인 경우, 각 data 사이에 출력할 문자열을 넣습니다. (기본값은 공백 한 칸 " "입니다.)

이때, end와 sep은 "end=", "sep="형식으로 인자를 전달해야합니다.

예시

print(1, 2, 3, end="")
print(4, 5, 6, sep="")

## 실행 결과 ##
1 2 3456
2. 메서드
Point I
특정 자료에 대해 특정 기능을 하는 코드
특정 자료.메서드이름(인자) 형태로 사용

Point II
함수 vs 메서드
함수 : 특정 기능을 하는 코드 (자료에 독립)
메서드 : 특정 자료에 대해 특정 기능을 하는 코드 (자료에 종속)

odd = [7, 2, 3, 5]

# 함수
max(odd)
print(odd)

# 메서드
odd.append(11)
odd.sort()