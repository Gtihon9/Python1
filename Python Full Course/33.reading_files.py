
try:
    with open('test.py') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")