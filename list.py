# 1. 리스트 생성
empty_list = []
list_with_items = [1, 2, 3]

# 2. 원소 접근, 수정
l = [3, 2, 56, 17, 42]
print(l[0], l[1], l[2], l[3], l[4])
print(l[-5], l[-4], l[-3], l[-2], l[-1])

l[0] = 15
l.append(100)
l.insert(1, 23)
del l[0]
l.pop()

# 3. 정렬
l = [3, 2, 56, 17, 42]
l.sort()
print(l)
# >>> [2, 3, 17, 42, 56]

l1 = [3, 2, 56, 17, 42]
l2 = sorted(l)
print(l1)
print(l2)
# >>> [3, 2, 56, 17, 42]
# >>> [2, 3, 17, 42, 56]

# comprehension
# 존재하는 리스트를 기반으로 새로운 리스트 생성
numbers = [i for i in range(10)]
print(numbers)
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = [i * 2 for i in range(10)]
odds = [i * 2 + 1 for i in range(10)]
print(evens)
print(odds)
# >>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# >>> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = [
    ('Jack', 75),
    ('Bob', 65),
    ('Ellie', 80),
    ('Hue', 95),
    ('Rick', 50)
]

honors = [student for student, score in result if score >= 80]
print(honors)
['Ellie', 'Hue']

# map
# 각 원소를 변환
l = [1, 2, 3, 4]
double = list(map(lambda n: n * 2, l))
print(double)
# >>> [2, 4, 6, 8]

# filter
# 조건이 성립되는 원소만을 포함하는 리스트 반환
l = [1, 2, 10, 7, 8, 17, 9, 5]
more_then_5 = list(filter(lambda n: n > 5, l))
print(more_then_5)
# >>> [10, 7, 8, 17, 9]

# reduce
# 각 원소에 대해서 정의된 동작을 누적으로 실행 -> 하나의 값 생성
from functools import reduce

scores = [75, 65, 80, 95, 50]
total = reduce(lambda a, b: a + b, scores)
print(total / len(scores))
# >>> 73.0