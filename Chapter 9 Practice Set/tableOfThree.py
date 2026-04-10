def generateTable(n):

    p = ""
    for i in range(1, 11):

        p += f"{n} * {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(p)

        f.close()


for j in range(2, 11):
    generateTable(j)
