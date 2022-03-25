from random import randint

print(*range(1, 11))
game_over = randint(1,10)
atterms = int(input())
while atterms > 0:
    player = int(input())
    if player == game_over:
        print('победа')
        break
    else:
        print('проигрыш')
    atterms -= 1



