n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())
set2 = set(map(int, input().split()))
unique_list = []
for i in set1:
    if i not in set2:
        unique_list.append(i)
for i in set2:
    if i not in set1:
        unique_list.append(i)
unique_list.sort()
for i in unique_list:
    print(i)