def print_formatted(number):
    width_field_bin = len(format(number,'b'))
    for _ in range(1,number+1):
        octal = format(_,'o')
        hexadecimal = format(_,'x')
        binary = format(_,'b')
        
        print(f'{str(_).rjust(width_field_bin)}{str(octal).rjust(width_field_bin + 1)}{str(hexadecimal).rjust(width_field_bin + 1)}{str(binary).rjust(width_field_bin + 1)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)