n=input()
score=list(map(int,input().split()))

max_score=max(score)
sum_score=0

for i in score:
    sum_score+=(i/max_score)*100

mean_score=sum_score/int(n)
print(mean_score)    
