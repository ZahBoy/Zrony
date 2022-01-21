import time
import random
from random import randint
a = 0
print ("░░░░░▐▀█▀▌░░░░▀█▄░░░")
print ("░░░░░▐█▄█▌░░░░░░▀█▄░░") 
print ("░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░") 
print ("░░░░▄▄▄██▀▀▀▀░░░░░░░ ")
print ("░░░█▀▄▄▄█░▀▀░░ Це")
print ('░░░▌░▄▄▄▐▌▀▀▀░░Скелетик')
print ('▄░▐░░░▄▄░█░▀▀ ░░Петя') 
print ('▀█▌░░░▄░▀█▀░▀ ░░') 
print ('░░░░░░░▄▄▐▌▄▄░░░') 
print ('░░░░░░░▀███▀█░▄░░ ')
print ('░░░░░░▐▌▀▄▀▄▀▐▄░░ ')
print ('░░░░░░▐▀░░░░░░▐▌░░') 
print ('░░░░░░█░░░░░░░░█░░░░░░░')
print ('░░░░░░█░░░░░░░░█░░░░░░░')
print ("	By ZahBoy")
time.sleep(2)
print("Гра полягає тому те що я загадую число від 0 до 100 і ти пробуєш вгадати")
time.sleep(3)
while a < 2:
	number = randint(0, 100)
	player_number = input('Я загадав число. Попробуй його вгадати ')
	player_number = int(player_number)
	while number != player_number:
		if 100 < player_number:
			print ('Я не загадую числа більші 100')
			player_number = input()
			player_numbrer = int(player_number)
		elif player_number < number:#Оператор еліф який якщо число менше ніж число яке загадав компютер
			print ('''Твоє число менше ніж моє.
Попробуй ще раз''')
			player_number = input()
			player_number = int(player_number)
		elif number < player_number:#Оператор еліф який якщо число більше ніж число яке загадав компютер
			print ('''Твоє число більше ніж моє.
Попробуй ще раз''')
			player_number = input()
			player_number = int(player_number)
	print ('''	Вітаю ти вгадав число
		''')
	time.sleep(2)