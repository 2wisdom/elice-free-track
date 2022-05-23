1. 리스트 활용
Point I
list.append(d) : 자료 d를 list의 마지막 원소 뒤에 추가

alphabet = ['A', 'B', 'C']
alphabet.append('D')
print(alphabet)

## 출력 결과 ##
['A', 'B', 'C', 'D']
Point II
list.insert(i, d) : 인덱스 i에 자료 d를 삽입

num_eng = ["one", "two", "four", "five"]
num_eng.insert(2, "three")
print(num_eng)

## 출력 결과 ##
["one", "two", "three", "four", "five"]
Point III
list.remove(d) : 인덱스 0부터 조회하여 처음 나오는 자료 d를 제거

ice_cream = ["Mother is Alien", "Mint Choco", "NY Cheese Cake", "Mint Choco"]
ice_cream.remove("Mint Choco")
print(ice_cream)

## 실행 결과 ##
["Mother is Alien", "NY Cheese Cake", "Mint Choco"]
Point IV
list.sort() : 리스트를 오름차순/사전순으로 정렬

digit = [0, 3, 6, 9, 1, 4, 7, 2, 5, 8]
digit.sort()
print(digit)

## 실행 결과 ##
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
2. 시퀀스 자료형
Point I
순서가 있는 자료형 → 리스트, 문자열 등이 이에 속함

Point II
인덱싱, 슬라이싱이 가능

prime_num = [2, 3, 5, 7, 9, 11]
prime_num[0] 
# 2

prime_num[1:4] 
# [3, 5, 7]
...
Point III
멤버 조회 in

prime_num = [2, 3, 5, 7, 9, 11]
2 in prime_num  
#True

4 in prime_num  
#False
Point IV
길이 확인 len

word = "Antidisestablishmentarianism"
len(word)  
#28
Point V
연결(+)과 반복(*)

mouse = ["Mickey"]
mice = mouse + ["Minnie"]  
#["Mickey", "Minnie"]

disney = ["Mickey"]*3 
#["Mickey", "Mickey", "Mickey"]