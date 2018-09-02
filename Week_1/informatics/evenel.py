n = int(input())
s = input().split(' ')
arr = [int(i) for i in s if int(i) % 2 == 0]
for i in arr:
    print(i, end = ' ')