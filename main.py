# print 함수

print("Hello World!")

# input 함수 이용
## 함수의 결과물(반환)을 변수에 담기

# name = input("당신의 이름을 입력하세요! >>> ")

# 메서드 : 특정 객체가 가지고 있는 함수를 의미. 특정 데이터 자료형에 포함되어 있는 함수 사실 함수와 메서드는 동일한 개념이지만, 호출 방식의 차이가 있다.
# 함수는 독립적으롷 ㅗ출할 수 있지만, 메서드는 특정 객체를 통해서만 호출할 수 있다.
# 즉 위의 print()와 input()은 함수

# eng_name = input("당신의 이름을 영어로 입력하세요. >>> ").lower() # .lower()는 메서드. -> input함수에 종속돼있다.

# 예를 들어 list 내에서 맨 뒤의 인덱스에 새로운 요소를 추가하는 .append()는 메서드라고 할 수 있음.
# 하지만 리스트이 요소의 합을 구할 수 있는 sum은 함수라고 할 수 있음.

li = [1, 2, 3]
print(li)
li.append(4)
print(li)
print(sum(li))

# str - 문자들을 줄로 엮어(string) 만들어 문자열이라고 번역 index / slice 가능
# Collection - 다양한 요소들을 한 번에 관리하기 위한 개념
#   list - 순서 있음 / index / slice / 추가, 수정, 삭제 가능
#   tuple - 순서 있음 / index / slice 가능 / 추가, 수정, 삭제 불가능
#   set - 순서 없음 / index / slice 불가능 / 추가, 수정, 삭제 가능 -> list와 함께 연계하여 중복 제거로 자주 쓰임.
#   dictionary - 순서 없음 / index / slice 불가능 / 추가, 수정, 삭제 가능 / 키 - 값의 쌍으로 이루어져 있음.

# 형변환
# age = input("당신의 나이를 입력하세요. >>> ")
# print(type(age))
# print(type(int(age)))

# 주석 처리 방법 - 한 줄 : ctrl + / / # / 여러줄 : '''     '''
# 함수

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("안녕")
  print("오늘 어때?")
  print("뭐해?")
greet()
def greet_with_name(name):
  print(f"안녕 {name}")
  print(f"오늘 어때, {name}?")
  print(f"뭐해, {name}")
greet_with_name("지우")

# Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet_with("Jack Bauer", "Nowhere")

greet_with(location = "Nowhere", name = "Jack Bauer")

# in : 포함 개념
li1 = [1, 2, 3, 4 ,5]
if 5 in li1:
    print("포함 되어 있지 않습니다.")

# not : 값 반전
should_continue = True
while should_continue:
    print("실행.")
    should_continue = False

print(should_continue)

if not should_continue:
    print("프로그램이 안전하게 정지됐습니다.")

li2 = []
for _ in range(3):
    li2.append("_")
print(li2)

li3 = []
for _ in range(4):
    li3 += "_"
print(li3)

# li3 = li3 + "_"
li3 = li3 + ["_"]

print(li3)

# 위의 반복문에서 이상한 점은 range()함수를 이용해서 생성한 값을 사용하지 않았다는 점입니다. range() 함수로 원하는 반복 횟수를 얻고자 할 때 쓰입니다.

for n in range(10):
    print("Hello")

# 이상의 함수는 변수 n을 선언했지만 실행문에서 n을 사용하는 코드는 없습니다. 이런 경우에는 '10번의 반복을 생성하는 코드'로 보여야 합니다.
# 즉 위의 예시는 "Hello" 출력을 10번 수행한다고 해석하시면 됩니다.

# 지역 변수 / 전역 변수

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지 
모든 경우의 수를 출력하도록 구현하세요.

함수 정의
- 반환값 : 없음
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine(money)
    #함수 구현

vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''


def vending_machine(money):
    price_per_drink = 700  # 음료수 한 잔의 가격
    max_drinks = money // price_per_drink  # 최대 구매 가능한 음료수 개수

    for i in range(max_drinks + 1):
        drinks = i
        change = money - (drinks * price_per_drink)
        print(f"음료수 = {drinks}개, 잔돈 = {change}원")


# 테스트 실행
vending_machine(3000)

'''
.value()메서드 설명해야함
키(key)가 "과목명", 값(value)이 "점수"인 marks 딕셔너리를 전달하면 해당 딕셔너리에 저장된 점수들의 평균을 반환하는 get_average() 함수를 구현하세요.

함수 정의
- 반환값 : 평균
- 함수 이름 : get_average()
- 매개변수 : 딕셔너리 marks

코드 구성
def get_average(marks):
    #함수 구현

marks = { "국어": 90, "영어": 80, "수학":85 }
average = get_average(marks)
print(f"평균은 {average}점입니다.)
'''
def get_average(marks):
    total = sum(marks.values())  # 모든 점수의 합을 계산
    count = len(marks)  # 과목의 개수
    average = total / count  # 평균 계산
    return average

# 테스트 실행
marks = { "국어": 90, "영어": 80, "수학": 85 }
average = get_average(marks)
print(f"평균은 {average}점입니다.")
