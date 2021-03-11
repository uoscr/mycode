from random import choice

def randoncapital(word):
    print(''.join(choice((str.upper, str.lower))(c) for c in word))

randoncapital("Oscar Rondon")

