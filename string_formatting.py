def print_formatted(number):
    width = len(str(bin(number))[2:])
    for num in range(1, number + 1):
        print(str(num).rjust(width, " "), end=" ")
        print(oct(num)[2:].rjust(width, " "), end=" ")
        print(hex(num).upper()[2:].rjust(width, " "), end=" ")
        print(str(bin(num))[2:].rjust(width, " "))


n = int(input(""))
if 1 <= n <= 99:
    print_formatted(n)
