import random

print('------------------login--------------------------------------------')
name = input("enter ur name: ")
age = input('enter age: ')
webpass = input('password: ')
command = f'''
welcome ({name},{age}) to world of game!
Even me(sidhant) developer doesnot know the 
correct guess ,its generated randomly.
best luck!
'''
print(command)
print('-----------------------start---------------------------------------')
count = 0
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

try:
  if webpass == 'sidhant':
          while num != number:
              n = input('guess: ')
              num = int(n)
              count += 1
              if num == number:
                  print('congratulations! u guess right')

              elif num < 35:
                  print('guess higher')

              elif num > 55:
                  print('guess lower')

              else:
                  print('closer!')
  else:
    print('enter correct password sent to u after registartion')

except ValueError:
  print('guess should be integer..start again..')


print('----------------------thanks-------------------------------------------')
print('done!')
print(out[number])


if num == number:
    for ch in n:
        op += out.get(ch, ch) + " "

print(f'correct guess is {op}')

if op == "":
  print('something went wrong')
else:
  if count == 1:
    print('wow! u r lucly! guessed in first attemp!')
  else:
      print(f'u took {count} step')

luck = 100-count
if op == "":
  print(f'luck meter: 0%')
else:
  print(f'luck meter: {luck}%')
print('-----------------------copyright @sidhantp-------------------------------')