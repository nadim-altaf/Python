with open("log.txt") as f:
    content = f.read()

if "bolean" in content:
    print("present")
else:
    print("not present")
