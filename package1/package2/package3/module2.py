# def good_word(name):
#     print( 'Ты лучший', name)

from package1.module1 import hello

def good_word(name):  # отсюда получать
    hello(name)  # сюда передавать
    print('Ты лучший', name)


if __name__ == '__main__':
    good_word('Урбан')
