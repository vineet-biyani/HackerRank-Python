def split_and_join(string_to_split):
    string_to_split = string_to_split.split()
    return '-'.join(string_to_split)


string = input("")
result = split_and_join(string)
print(result)
