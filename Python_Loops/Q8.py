#Pattern - 1
#          121
#          12321
#          1234321

n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = "")

    for k in range(i-1, 0, -1):
        print(k, end="")

    print()