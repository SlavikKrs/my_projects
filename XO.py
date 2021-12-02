
def game_field():
    print('  0 1 2')
    for i in range(len(field)):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")


def player_move():
    while True:
        place = input("Ваш ход?").split()

        if len(place) !=2:
            print("введите координаты правильно")
            continue

        x, y = place

        if not(x.isdigit()) or not(y.isdigit()):
            print("введите цифры")
            continue
        x, y = int(x), int(y)

        if x < 0 or y < 0 or x > 2 or y > 2:
            print("координаты вне игрового поля")
            continue

        if field[x][y] != " ":
            print("эта клетка занята")
            continue

        return x, y

def who_win():
    winners = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for a in winners:
        symbols = []
        for c in a:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print('Выиграл "X" ')
            return True
        if symbols == ["0", "0", "0"]:
            print('Выиграл "0" ')
            return True
    return False



print("крестики-нолики")
print("введите координаты хода через пробел")
print("первая - по вертикали")
print("вторая - по горизонтали")

field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    game_field()
    if count % 2 == 1:
        print(' Ход "X" ')
    else:
        print(' Ход "O" ')

    x, y = player_move()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if who_win():
        break

    if count == 9:
        print(" Ничья!")
        break