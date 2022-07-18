import random
from random import *
from string import punctuation

special_chars = list(punctuation) # 32 Elements in list
password = ""
length = input("Input length of password\n: ")


for i in range(int(length)):
    a = chr(randint(65, 90))
    b = chr(randint(65, 90)).lower()
    c = special_chars[randint(0, 31)]
    
    password = password + str(a) + str(b) + str(c)
    
print(''.join(sample(password, len(password))))

