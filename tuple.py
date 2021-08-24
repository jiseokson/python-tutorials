# 1. 튜플
t = (1, 2, 3)
rgb = ('red', 'green', 'blue')

print(rgb[0])
# TypeError: rgb[0] = 'RED'
# 튜플의 값은 수정할수 없음! (Immutable)

# 2. 튜플을 원소로 가지는 리스트의 순회
students = [('Jiseok', 23), ('jack', 21)]
for name, age in students:
    print(name, age)