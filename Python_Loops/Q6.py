# Calculate 1/1! + 2/2! + 3/3! + .....

n = int(input("Enter your number: "))
ans = 0
fact = 1
for i in range(1,n+1):
    fact = fact*i
    ans = ans + i/fact

print("The answer is: ", ans)