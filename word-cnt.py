content = '''
Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti assumenda illum magni sint veniam iste corporis in molestiae sed expedita id dicta modi, reprehenderit quo!
Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veritatis aspernatur ipsa voluptatibus temporibus dolores voluptatem id minus at quisquam eos.
Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero beatae deserunt, possimus modi sint voluptatibus odio cupiditate eaque sequi iste ea eligendi labore aut maiores, inventore suscipit. Earum, fugiat eligendi.
Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sit numquam enim voluptatum optio, deleniti iste quasi cupiditate.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique eos laboriosam odit nam labore illo?
Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt ipsam architecto, deserunt fuga exercitationem optio eaque fugit.
'''

words = {}
for line in content.split('\n'):
    line = line.strip()
    for word in line.split(' '):
        word = word.strip()
        if word == '':
            continue
        words[word] = words.get(word, 0) + 1

for word, count in words.items():
    print(f"'{word}': {count}")