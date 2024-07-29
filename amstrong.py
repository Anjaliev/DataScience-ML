for n in range(1,1001):
    num=n
    number=str(n)
    nlen=len(number)
    sum=0
    while n>0:
        d=n%10
        sum=sum+d**nlen
        n=n//10
    if sum==num:
        print(num)