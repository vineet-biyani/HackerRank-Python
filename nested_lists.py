n = int(input(""))

if 2 <= n <= 5:
    scores = [[input(""), float(input(""))] for num in range(0, n)]
    scores.sort(key=lambda lst: lst[-1])
    lowest_score = scores[0][1]
    second_lowest_score = 0
    for score in scores:
        if score[1] > lowest_score:
            second_lowest_score = score[1]
            break
    second_lowest_scores = [score for score in scores if score[1] == second_lowest_score]
    second_lowest_scores.sort(key=lambda lst: lst[0])
    for name, score in second_lowest_scores:
        print(name)
