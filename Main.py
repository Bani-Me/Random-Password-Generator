import random
password = []

def Random_num1():
 global password
 n = random.randrange(1,100000)
 n = int(str(n)[:2])
 password.append(n)

def Random_lowchar():
    global password
    keyboard_characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '`', '-', '[', ']', ';', '!', '@', '#', '$', '%', '^', '&', '*', '?'
    ]

    i = 0
    while i < 2:
     x = random.randrange(0, len(keyboard_characters))
     y = keyboard_characters[x]
     if x < 26:
         j = random.randrange(0,2)
         if j == 1:
          y = y.upper()

     password.append(y)
     i +=1






k = 0
while k < 4:
 Random_num1()
 Random_lowchar()
 k += 1

result = ''.join(map(str,password))
print("The generated password is: " + result)

