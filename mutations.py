def mutate_string(string_value, i, character):
    string_value = list(string_value)
    string_value[i] = character
    return ''.join(string_value)


string = input("")
index, char = input("").split()
result = mutate_string(string, int(index), char)
print(result)
