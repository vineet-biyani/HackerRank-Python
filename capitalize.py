def capitalize(old_string):
    string_list = [word.capitalize() for word in old_string.split(" ")]
    return " ".join(string_list)


string = input("")


if 0 < len(string) < 1000:
    print(capitalize(string))
