from random import randint
key=''
keys=''
final=''
mes = input("Введите сообщение, которое хотите зашифровать: ")
for symbol in mes:
    key = randint(0,32); keys += str(key) + "/"
    final += chr((ord(symbol) + key - 17)%33 + ord('А'))
print('Зашифрованное сообщение: ', final)
print ('Ключ шифрования: ',keys)
 
print('Введите зашифрованное сообщение: ')
final=input()
print ('Введите ключ шифрования: ')
keys = input()
keys =  keys.split('/')
mes = ''
for i, symbol in enumerate(final):
    if keys[i] != '':
        mes += chr((ord(symbol) - int(keys[i])- 17)%33 + ord('А'))
print ('Расшифрованное сообщение : ', mes)

