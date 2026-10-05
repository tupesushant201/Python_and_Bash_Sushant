file = open("notes.txt", "r")

content = file.read()

file.close()

print("Content of notes.txt:")
print(content)