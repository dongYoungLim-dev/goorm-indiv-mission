
# list
# 문제1: 1부터 5까지의 숫자를 담은 리스트를 만들고, 3번째 요소를 출력하세요.
# 문제2: 빈 리스트에 'apple', 'banana', 'cherry'를 순서대로 추가한 뒤, 리스트의 길이를 출력하세요.

# 답변 코드
# 문제 1
list = [1, 2, 3, 4, 5]
print(list[2])

# 문제 2
list2 = []
list2.append('apple')
list2.append('banana')
list2.append('cherry')

print(len(list2))

# dict
# 문제1: 이름을 키로, 나이를 값으로 갖는 딕셔너리 {'철수': 20, '영희': 22}를 만들고, '철수'의 나이를 출력하세요.
# 문제2: 빈 딕셔너리에 'city': '서울', 'population': 9700000을 추가하고, 'city' 키의 값을 출력하세요.

# 답변코드
# 문제1
dict = {'철수': 20, '영희': 22}
print(dict['철수'])

# 문제 2
dict2 = {}
dict2['city'] = '서울'
dict2['population'] = 9700000

print(dict2['city'])

# string
# 문제1: "Hello, Python!" 문자열에서 'Python'만 슬라이싱하여 출력하세요.
# 문제2: "  hello  " 문자열의 앞뒤 공백을 제거하고, 대문자로 변환하여 출력하세요.

# 답변코드
# 문제 1
str = 'Hello, Python!'
print(str[7:12])

# 문제 2
str2 = '  hello  '
str2_strip = str2.strip() # 앞뒤 공백 제거
str2_upper = str2.upper() # 대문자 변환
print(f"공백 제거 : {str2_strip}, 대문자 변환 : {str2_upper}")

# 문자열 포멧팅
# 문제1: 변수 name='김철수', age=25를 f-string으로 "이름: 김철수, 나이: 25" 형태로 출력하세요.
# 문제2: format() 메서드를 사용하여 "{} + {} = {}" 형태로 10, 20, 30을 출력하세요.

# 답변코드
# 문제 1
name = '김철수'
age = 25
print(f"이름: {name}, 나이: {age} 세")
print("이름: %s, 나이: %d 세" % (name, age))
print("이름: {0}, 나이: {1} 세".format(name, age))
print("이름: {name}, 나이: {age} 세".format(name=name, age=age))

# 문제 2
a = 10
b = 20
c = 30
print("{} + {} = {}".format(a, b, c))

# 리스트 컴프리헨션
# 문제1: 1부터 10까지의 숫자 중 짝수만 담은 리스트를 리스트 컴프리헨션으로 만드세요.
# 문제2: ['apple', 'banana', 'cherry'] 리스트의 각 요소의 길이를 담은 새 리스트를 리스트 컴프리헨션으로 만드세요.

# 답변코드
list = ['apple', 'banana', 'cherry']

# 문제 1
list2 = [i for i in range(1, 11) if i % 2 == 0]
print(list2)

# 문제 2
list3 = [len(i) for i in list]
print(list3)
