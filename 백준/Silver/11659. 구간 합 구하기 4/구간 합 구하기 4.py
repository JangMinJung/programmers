import sys
input= sys.stdin.readline
N,M=map(int,input().split())
arr=list(map(int, input().split()))
sum_arr=[0]
start=0
for i in arr:
    start+=i
    sum_arr.append(start)

for i in range(M):
    s,e=map(int,input().split())
    print(sum_arr[e]-sum_arr[s-1])