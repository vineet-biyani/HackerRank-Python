n = int(input(""))

if 2 <= n <= 10:
    student_scores = {}
    for _ in range(0, n):
        name, *scores = input("").split()
        student_scores[name] = [float(score) for score in scores if 0 <= float(score) <= 100]
    query_name = input("")
    scores_to_average = student_scores.get(query_name, None)
    if scores_to_average is not None:
        print('{:.2f}'.format((sum(scores_to_average)) / len(scores_to_average)))
