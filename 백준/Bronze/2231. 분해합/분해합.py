N = int(input())
found = False

for num in range(1, N+1):
    total = num + sum(map(int, str(num)))
    if total == N:
        print(num)
        found = True
        break

if not found:
    print(0)
