def wrap(string_to_wrap, max_width):
    wrapped_list = [string_to_wrap[i:i + max_width] for i in range(0, len(string_to_wrap), max_width)]
    return '\n'.join(wrapped_list)


string = input("")
width = int(input(""))

if (0 < len(string) < 1000) and (0 < width < len(string)):
    result = wrap(string, width)
    print(result)


# ALTERNATE METHOD 1
import textwrap


def wrap(wrapping_string, wrapping_width):
    return '\n'.join(textwrap.wrap(wrapping_string, wrapping_width))


string = input("")
width = int(input(""))
if (0 < len(string) < 1000) and (0 < width < len(string)):
    result = wrap(string, width)
    print(result)


# ALTERNATE METHOD 2
def wrap(string_for_wrapping, wrap_width):
    new_string = ''
    for i in range(0, len(string_for_wrapping), wrap_width):
        new_string = new_string + string_for_wrapping[i:i+wrap_width] + '\n'
    return new_string.strip()


string, width = input(), int(input())
if (0 < len(string) < 1000) and (0 < width < len(string)):
    result = wrap(string, width)
    print(result)
