import random

para1 = random.randrange(3, 20)
pass1 = []
print('Первое поле:', para1)

for i in range(1, para1):
    for j in range(i+1, para1):
        if int(para1) % (int(i) + int(j)) == 0:
            pass1.extend([i, j])
print('Пароль:', ''.join(map(str, pass1)))