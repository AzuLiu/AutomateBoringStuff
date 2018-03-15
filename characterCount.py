message = input('Message: ')
count={}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

print(count)
