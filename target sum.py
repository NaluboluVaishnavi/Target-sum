a = list(map(int,input().split()))
t = int(input())
a.sort()
i=0
j=len(a)-1
ans=0
while i<j:
    curr_sum = a[i]+a[j]
    if curr_sum==t:
        print(i,j)
        i +=1
        j -=1
    elif curr_sum<t:
        i = i+1
    else:
        j = j-1