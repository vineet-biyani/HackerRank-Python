n = int(input(""))

if 1 <= n <= 100:
    if (n % 2 != 0) or (n % 2 == 0 and (6 <= n <= 20)):
        print("Weird")
    else:
        print("Not Weird")
