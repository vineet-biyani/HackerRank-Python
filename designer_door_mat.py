n, m = map(int, input("").split())
character = '.|.'
message = 'WELCOME'

if (5 < n < 101) and (15 < m < 303):
    for i in range(0, (n//2)):
        print((character * ((2 * i) + 1)).center(m, '-'))
    print(message.center(m, '-'))
    x = i + 2
    for i in range((n//2)+1, n):
        print((character * ((2 * x) - 3)).center(m, '-'))
        x -= 1
