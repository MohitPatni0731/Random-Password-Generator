from sys import argv
from math import *
import pylance
import sql 
import random
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
try:
    password_len = int(input("What length would you like your password to be -"))
except:
    print("Wrong Input, Type Integer only")
    pass
try:
    password_count = int(input("How many password would you want -"))
except:
    print("Wrong Input, Type Integer only")
    pass
for x in range(0,password_count):
    password = ""
    for x in range(0,password_len):
        password_char = random.choice(character)
        password = password + password_char
    print("Here you go -", password)
if password_len == str:
    print("Wrong")
