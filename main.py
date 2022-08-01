import PySimpleGUI as sg
from random import choice
import string


def __init__(self):
    pass

def password_size(self):
    pass
#password_size = int(input('Password Length  '))
charpassword = string.ascii_letters + string.digits + string.punctuation

safety_password = ''
for i in range(password_size):
    safety_password += choice(charpassword)

print('The safety password generate is ', safety_password)
