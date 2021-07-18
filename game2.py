import random

command = '''
welcome to world of game!
Even me(sidhant) developer doesnot know the 
correct guess ,its generated randomly.
best luck!
'''
print(command)

op = ""
num = ''
number = random.randint(40,50)
out = {
    number:'👌👏',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero'
}

while num != number:
    n = input('guess: ')
    num = int(n)
    if num == number:
        print('congratulations! u guess right')

    elif num < 35:
        print('guess higher')

    elif num > 55:
        print('guess lower')

    else:
        print('closer!')

print('done!')
print(out[number])

if num == number:
    for ch in n:
        op += out.get(ch, ch) + " "

print(f'correct guess is {op}')
