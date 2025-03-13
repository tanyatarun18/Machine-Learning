# Find the sum of 3 digit number entered by user.

a = int(input("Enter your number: "))
sum1 = 0

while a > 0 :
    digit = a%10
    sum1 = sum1 + digit
    a = a//10

print(sum1)