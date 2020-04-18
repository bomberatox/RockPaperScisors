from random import randint

play: bool = True
while play == True:
    print('(1) Rock    (2) Paper')
    e = int(input('(3) Scissor (4) Exit\n'))
    c = randint(1, 3)
    if e == 4:
        play = False
    elif e == c:
        print('I choose this one too!\n\033[33mIts a draw!\033[m\nWanna play again?')
    elif e == 1 and c == 2:
        print('I choose paper!\n\033[31mYou lose!\033[m\nWanna play again?')
    elif e == 1 and c == 3:
        print('I choose scissor!\n\033[32mYou won!\033[m\nWanna play again?')
    elif e == 2 and c == 1:
        print('I choose rock!\n\033[32mYou won!\033[m\nWanna play again?')
    elif e == 2 and c == 3:
        print('I choose scissor!\n\033[31mYou lose!\033[m\nWanna play again?')
    elif e == 3 and c == 1:
        print('I choose rock!\n\033[31mYou lose!\033[m\nWanna play again?')
    elif e == 3 and c == 2:
        print('I choose paper!\n\033[32mYou won!\033[m\nWanna play again?')
