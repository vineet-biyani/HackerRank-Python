n = int(input(""))

if 2 <= n <= 10:
    scores = list(map(int, input("").split()))
    scores.sort(reverse=True)
    for num in scores:
        if num < scores[0]:
            print(num)
            break
