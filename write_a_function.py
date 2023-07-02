def is_leap(is_year_leap):
    if is_year_leap % 400 == 0 or (is_year_leap % 4 == 0 and is_year_leap % 100 != 0):
        return True
    return False


year = int(input(""))
print(is_leap(year))
