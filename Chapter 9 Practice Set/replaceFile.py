word = "python"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "java")

with open("file.txt", "w") as f:
    f.write(contentNew)
