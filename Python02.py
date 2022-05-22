#1. 입력

#변수 = input() : 변수에 입력받은 값을 집어넣겠다는 의미

var = input()


#[실습1] 따라쟁이 앵무새
# input()을 이용해서 입력을 넣고, 이를 변수 var에 담아봅시다.
var = input()

# 앵무새가 말을 따라합니다!
print("앵무새 :", var)

# 입력한 값이 어떤 자료형인지 확인해봅시다.
print(type(var))


#어떤 것을 입력하든 문자열로 입력되기 때문에 형 변환이 필요
#int() : 정수형 변환, str() : 문자열 변환 등…

var1 = input() #4 입력
var1 = int(var1)
var2 = int(input()) #3 입력
print(3+var1+var2) #10 출력


#[실습2] 2배로 적금

#변수 money에 input을 이용해서 입력을 받아봅시다.
money = input()

# money를 int형으로 변환해서, 다시 money에 넣어줍시다.
money = int(money)

# money를 2배 불려서 print로 출력해봅시다.
print(money * 2)


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


#[실습3] 명제 만들기

# Q1. == 혹은 != 연산자을 이용해서 True인 명제를 ans1에 넣어봅시다.
ans1 = 1 == 1

# Q2. > 혹은 < 연산자를 이용해서 False인 명제를 ans2에 넣어봅시다.
ans2 =  1 > 2

# Q3. >= 혹은 <= 연산자를 이용해서 True인 명제를 ans3에 넣어봅시다.
ans3 = 1 >= 1

# 위의 세 변수를 출력해서 True, False 여부를 확인해봅시다.
print(ans1, ans2, ans3)



#논리 연산자 : 논리 자료형 사이의 연산

AND : 각 논리가 모두 True이면 결과가 True  
OR : 각 논리 중 True가 존재하면 결과가 True  
NOT : 논리값을 뒤집는 연산


#[실습4] 빈칸 추론

# 괄호 안에 적절한 명제를 채워 stat1이 True가 되게 해봅시다.
stat1 = 3==3 and 2<4 and (3 != 2)

# 괄호 안에 적절한 명제를 채워 stat2이 False가 되게 해봅시다.
stat2 = 4>=6 or "apple"=="Apple" or (21 > 30) 

# 괄호 안에 적절한 명제를 채워 stat3이 True가 되게 해봅시다.
stat3 = not ("lizzie" == "Lizzie")

# 위의 세 변수를 한 문장으로 출력해서 True, False 여부를 확인해봅시다.
print(stat1, stat2, stat3)


#3. 조건문

#조건에 따라 특정 명령을 수행하는 구문

#if문 : 조건이 참이면 명령을 수행

if a >= 5:
    print("a는 5 이상입니다!")


#[실습5] 홀짝판별기

# input()을 이용해서 숫자(정수) 입력을 받고, 변수 num에 이를 넣어봅시다.
num = int(input())


# if-else문을 이용해서 만약 입력받은 수가 홀수면 "(입력받은 수) 홀수입니다."
# 짝수면 "(입력받은 수) 짝수입니다."를 출력해봅시다.
# 괄호는 출력하지 않습니다.

if num % 2 != 0 :
    print(num, "홀수입니다.")
else :
    print(num, "짝수입니다.")


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


#[실습6] 업-다운 게임

# 변수 answer에 수 1~50 중 하나를 넣어봅시다.
answer = 50

# input을 통해 숫자형으로 입력을 받아서 변수 submit에 저장해봅시다.
submit = int(input())

# if-elif-else문으로 Up-Down Game을 구현해봅시다.
# 만약 answer보다 submit이 더 크면 "정답보다 더 큰 수를 입력했습니다."
# 만약 answer보다 submit이 더 작으면 "정답보다 더 작은 수를 입력했습니다."
# 만약 answer와 submit이 같으면 "정답!" 를 출력합니다.

if answer < submit : print("정답보다 더 큰 수를 입력했습니다.")
elif answer > submit : print("정답보다 더 작은 수를 입력했습니다.")
else : print("정답!")


#[미션1] 자리수 판별기

# 1~999까지의 숫자 중 하나가 입력될 때,

# 1자리(1~9)이면 "한 자리 숫자입니다."
# 2자리(10~99)이면 "두 자리 숫자입니다."
# 3자리(100~999)이면 "세 자리 숫자입니다."
# 를 출력해봅시다.

# 변수 num을 선언하고, 숫자형으로 입력을 받습니다.
num = int(input())

# if-elif-else문을 이용해서 조건에 따라 출력합니다.
# 왼쪽에 있는 조건에 따라 자리수를 출력해봅시다.
if num < 9 : print("한 자리 숫자입니다.")
elif num < 100 : print("두 자리 숫자입니다.")
else : print("세 자리 숫자입니다.")


#[미션2] 교수님 마음으로

# 코더랜드에 있는 E대학의 J교수님은 학점을 잘 주시는 것으로 유명합니다.

# 이 교수님은 시험 점수가 77점 이상이면 학생에게 A0(숫자 0)를 주시고, 88점 이상이면 A+를 부여합니다.

# 단, 이 교수님은 성의가 없는 학생을 싫어하셔서 시험 점수가 0점인 학생에게 가차없이 F를 부여합니다. 위 경우에 모두 해당하지 않는 학생들에게는 전부 B+를 부여합니다.

# 어떤 학생의 시험 점수가 입력되면 이 학생의 학점을 출력하는 프로그램을 작성해봅시다.

#주어진 미션을 수행해볼까요?
num = int(input())

if num == 0 : print('F')
elif 88 > num >= 77 : print('A0') # 88 > num > 77
elif num >= 88 : print('A+') # num > 88
else : print('B+')