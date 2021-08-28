content = '''
The US Embassy in Kabul on Friday again warned US citizens at a number of gates at Hamid Karzai International Airport to "leave immediately," citing security threats.
The alert advised US citizens "to avoid traveling to the airport and to avoid airport gates."
Flights could be seen taking off Saturday but it was unclear how many people were being allowed into the airport.
An eyewitness told CNN he saw Taliban members fire shots in the air outside the main Kabul airport entrance gate on Saturday morning to disperse crowds that had gathered again in attempts to flee Afghanistan.
Far fewer people were at the airport Friday, and a source directly familiar with the Kabul airport operations told CNN the remaining focus was to get people with special, last-minute access requests to the airport. But the source cautioned that officials were "unsure how many they can get in with so much Taliban coordination required."
'''

words = {}
for line in content.split('\n'):
    line = line.strip()
    for word in line.split(' '):
        word = word.strip()
        word = word.lower()
        if word == '':
            continue
        words[word] = words.get(word, 0) + 1

for word, count in words.items():
    print(f"'{word}': {count}")