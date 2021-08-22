# 1. 함수 정의
def mean(a, b, c):
    res = (a + b + c) / 3
    return res

# 2. Default parameters
def greeting(name, cnt = 1):
    for _ in range(cnt):
        print(f'My name is {name}!')

greeting('Jiseok')
greeting('Tas', 5)

# 3. Keyword arguments
def solve(a, b):
    '''방정식 ax + b = 0의 해를 반환'''
    return -b / a

print(solve(2, 10))
print(solve(b = 10, a = 2))

print('This', 'is', 'print', 'function')
print('This', 'is', 'print', 'function', 'with', 'sep', 'option', sep = '-')

# 4. 재귀함수
# 함수의 정의에 자신이 포함되는 형식의 함수

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 5. 익명함수
def do_something(l, fn):
    for item in l:
        fn(item)
    
do_something([1, 2, 3], lambda item: print(item * 2))