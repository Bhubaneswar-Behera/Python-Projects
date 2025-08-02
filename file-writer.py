with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)


with open('sample.txt', 'w') as file:
    file.write("Adding something to the file")

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)    