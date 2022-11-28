import random


def password_generate():
    pas = ''
    for x in range(9):
        pas += random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return pas