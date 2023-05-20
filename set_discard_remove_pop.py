number_of_elements = int(input())
elements = set(map(int, input().split()))

number_of_commands = int(input())
list_of_commands = []

for _ in range(number_of_commands):
    list_of_commands.append(input().split(' ', 3))
    
for _ in list_of_commands:
    if _[0] == 'pop':
        elements.pop()
    elif _[0] == 'remove':
        elements.remove(int(_[1]))
    elif _[0] == 'discard':
        elements.discard(int(_[1]))
        
print(sum(elements))