n = int(input())
arr = [str(i ** 2) for i in range(1, n + 1) if i ** 2 <= n]
print (' '.join(arr))