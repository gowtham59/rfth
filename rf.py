n1=int(input())
k2=list(map(int,input().split()))
s3=[1]*n1
for i in range(n1):
    if i==0:
        if k2[i]>k2[i+1]:
            s3[i]=s3[i]+s3[i+1]
    elif i>0:
        if k2[i]>k2[i-1]:
            s3[i]=s3[i]+s3[i-1]
print(sum(s3))
