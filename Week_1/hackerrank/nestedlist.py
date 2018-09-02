arr = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    arr[name] = score
a = sorted(arr.items(), key=lambda kv: kv[1])
res = 0
for i in range(len(a)-1):
    if a[i][1] != a[i+1][1]:
        res = a[i+1][1]
for i in range(len(a)-1):
    if res == a[i][1]:
        print(a[i][0])