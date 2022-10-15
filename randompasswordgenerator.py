import string
import random

alphabet = string.ascii_letters
number = string.digits
special_char = string.punctuation
pwd = alphabet + number + special_char
password =""
x = int(input("enter length of password that you want to create:"))
'''i=1
while i <= x:
    password = password + random.choice(pwd)
    i+=1'''
for i in range(x):
    password = password + random.choice(pwd)
print(f"your password is : {password}")    
 