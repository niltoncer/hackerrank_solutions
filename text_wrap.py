import textwrap

def wrap(string, max_width):
    max_width = textwrap.TextWrapper(width = max_width)
    print(max_width)
    string = max_width.wrap(string)
    return "\n".join(string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)