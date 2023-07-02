def swap_case(string_to_swap):
    swapped_list = [char.upper() if char.islower() else char.lower() for char in string_to_swap]
    return ''.join(swapped_list)


string = input("")
if 0 <= len(string) <= 1000:
    result = swap_case(string)
    print(result)
