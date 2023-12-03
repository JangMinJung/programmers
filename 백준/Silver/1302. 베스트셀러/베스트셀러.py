from collections import Counter
a = int(input())
b = []
for i in range(a):
	title = input()
	b.append(title)
c = Counter(b)
max_value = max(c.values())
max_list =[]
for key, value in c.items():
    if value == max_value :
        max_list.append(key)
max_list.sort()

print(max_list[0])
        
