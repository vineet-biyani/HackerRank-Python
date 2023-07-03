def count_substring(base_string, string_to_count):
    substring_length = len(string_to_count)
    substring_list = [base_string[i:i+substring_length] for i in range(0, len(base_string)-substring_length+1)]
    return substring_list.count(string_to_count)


string = input("")
sub_string = input("")

if 0 <= len(string) <= 200:
    count = count_substring(string, sub_string)
    print(count)
