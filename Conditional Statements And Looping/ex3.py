import random 

target_num,guess_num = random.randint(1,10),0

while target_num!= guess_num:
    guess_num = int(input('Guess number between 1 to 10:'))
print('Well guessed')