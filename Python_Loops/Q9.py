#Find prime number between a certain rangw.

lower = int(input("Enter your lower range: "))
upper = int(input("Enter your upper range: "))

for i in range(lower, upper+1):
    for j in range(2, i):
        if(i%j == 0):
            break
    else:
        print(i)