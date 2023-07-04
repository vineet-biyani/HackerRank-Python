thickness = int(input(""))
character = 'H'

if (0 < thickness < 50) and thickness % 2 != 0:
    for i in range(0, thickness):
        print((character * ((2 * i) + 1)).center(thickness * 2, ' '))
    for i in range(0, thickness + 1):
        print((character * thickness).center(thickness * 2, ' ') + (character * thickness).center(thickness * 6, ' '))
    for i in range(0, (thickness // 2) + 1):
        print((character * thickness * 5).center(thickness * 6, ' '))
    for i in range(0, thickness + 1):
        print((character * thickness).center(thickness * 2, ' ') + (character * thickness).center(thickness * 6, ' '))

    x = thickness
    for i in range(0, thickness):
        print((character * ((2 * x) - 1)).center(thickness * 2, ' ').rjust(thickness * 6, ' '))
        x -= 1
