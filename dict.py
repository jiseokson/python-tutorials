# 1. 딕셔너리 Dictionary
# key-value pair collection

empty_dict = {}
new_dict = dict()
attribute = {
    'size': 24, 
    'font': 'roboto',
    'color': 0xff341a
}

# 2. 접근 Accessing
print(attribute['size'])
print(attribute['font'])
print(attribute['color'])

words = {
    'the': 24,
    'a': 32,
    'new': 12,
    'nation': 7
}

the = 'the'
print(f"'the': {words.get('the', 0)}")
print(f"'president': {words.get('president', 0)}")

# 3. 추가 Add, 수정 Modifying, 삭제 Removing
person = {'name': 'Bob'}
person['gender'] = 'Male' # add
person['name'] = 'Jiseok' # modifying
del person['gender']

# 4. 순회 Looping
player = {
    'id': 'sparrrk',
    'level': 24,
    'name': 'Jiseok Son',
    'active': True
}

for key, value in player.items():
    print(key, value)

for key in player.keys():
    print(key)

for value in player.values():
    print(value)