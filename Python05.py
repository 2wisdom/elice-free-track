1. 시퀀스 활용하기
Point I
list.pop(i) : 인덱스 i의 원소를 제거 후 반환

lst = [1, 2, 3, 4, 5]
box = lst.pop(0) # lst에서 1을 제거 후 반환, 이 경우에는 변수 box에 대입
print(lst) 
# [2, 3, 4, 5]

print(box)
# 1 
Point II
seq.count(d) : 시퀀스 내부의 자료 d의 개수를 반환

carrot = "Hi Rabbit!"
print(carrot.count("i"))

## 실행 결과 ##
2
Point III
str.split(c) : 문자열 c를 기준으로 문자열 str을 쪼개서 리스트를 반환

ours = "나,너,우리"
print(ours.split(","))
# ['나', '너', '우리']
Point IV
str.join(list) : str을 기준으로 list를 합쳐서 문자열을 반환

coffee = ['a', 'm', 'e', 'r', 'i', 'c', 'a', 'n', 'o']
print("".join(coffee)) # 빈 문자열("")을 기준으로 합치기
# americano
2. Tuple(튜플)
Point I
여러 자료를 담을 수 있으면서, 변하지 않는 자료형

Point II
() - 소괄호로 묶어 표현

tup = (1, 2, 3, 4, 5)
Point III
원소가 하나라면 반드시 원소 뒤에 ,을 적어주어야함

tup_one = (1,)
Point IV
시퀀스 자료형의 성질을 지님

cute = ('c', 'a', 't')
print(cute[1])  #인덱싱
#'a'

print(cute[1:]) #슬라이싱
#('a', 't')

print('e' in cute) #in연산자
#False

print(len(cute)) #len연산자
#3

print(cute + ('e', 'g', 'o', 'r', 'y')) #연결연산
#('c', 'a', 't', 'e', 'g', 'o', 'r', 'y')

print(cute * 3) #반복연산
#('c', 'a', 't', 'c', 'a', 't', 'c', 'a', 't')
Point V
자료를 추가, 삭제, 변경할 수 없다!

hero = ("ant", "man")
hero.append("wasp") #Error
hero.remove("man") #Error
hero[0] = "iron" #Error
3. Dictionary(사전형)
Point I
짝꿍(Key → Value)이 있는 자료형

Point II
{} - 중괄호로 묶어서 표현

hp = {"gildong" : "010-1234-5678"}
Point III
key를 알면 value를 알 수 있다.

dic = {"apple":"사과", "banana":"바나나"}
print(dic["apple"])
# 사과
Point IV
del 키워드로 Dictionary의 원소 삭제
리스트의 원소를 삭제하는 것도 가능!

dic = {"apple":"사과", "banana":"바나나"}
del dic["apple"]
print(dic)
# {"banana":"바나나"}
Point V
Key는 변할 수 없는 자료형이여야 한다

dic = {[1, 3, 5]:"odd"} #Error
dic = {(2, 4, 6):"even"} 


# [미션1]

# Bello, Tulaliloo ti amo!
# 영화 <슈퍼 배드>에 나오는 미니언즈는 Minionese라고 하는 신기한 언어를 사용합니다.
# 우리가 미니언 용어를 모르기 때문에 Minionese를 한국어로 번역해주는 사전을 하나 만들고자 합니다.

# 아래 미니언 용어 사전을 참고해서
# key = Minionese, value = 한국어인 Dictionary를 변수 miniWord에 담아봅시다.

# Minionese	한국어
# Bello	안녕
# Poopaye	잘가
# Tank_yu	고마워
# Tulaliloo_ti_amo	우린 너를 사랑해

cvs = ["Bello", "Bello", "Tulaliloo_ti_amo", "Tank_yu", "Poopaye", "Poopaye"]

# Minionese와 한국어가 담긴 miniWord 딕셔너리를 만드세요.
miniWord = { 'Bello' : '안녕', 'Poopaye' : '잘가', 'Tank_yu' : '고마워', 'Tulaliloo_ti_amo' : '우린 너를 사랑해' }

for i in cvs :
    print(miniWord[i])