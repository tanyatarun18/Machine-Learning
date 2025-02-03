#Print the multiplicaiton table for a given number up to 10

# a = int(input("Enter the num: "))
#
# for i in range(1,11):
#     mul = a*i
#
#     print (mul)


#Now suppose in last question we want to skip certain iteration let say we want to skip 5th iteration
a = int(input("Enter the num: "))

for i in range(1,11):
    if(i == 5):
        continue
    mult = a * i

    print(mult)