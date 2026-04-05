for i in range(50):
    if i == 20:
        break # exit the loop right now
    print(i)

for i in range(50):
    if i == 20:
        continue # skip this iteration
    print(i)

# PASS STATEMENT 

for j in range(3):
    pass   # It instructs to “do nothing”.
 
# without pass, the program will throw an error  

a = 1
while(a<=10):
    print(a)
    a+=1
