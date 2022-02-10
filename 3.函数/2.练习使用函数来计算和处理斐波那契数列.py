def fib(n):
    i=1
    a,b=1,1
    while i<n:
        a,b=b,a+b
        i=i+1
    return a
print(fib(10))

def remainder1(n):
    for i in range(2,1+n):
        num=(fib(1)%i,fib(2)%i)
        j=2
        while num!=(fib(j)%i,fib(j+1)%i):
            j=j+1
        print("fib数列对",i,"的余数数列的周期为",j-1)

#remainder1(5000)

def remainder2(n):
    L=[1]
    for i in range(2,n+1):
        a,b=fib(2)%i,fib(3)%i
        j=2
        while (a,b)!=(1,1) :
            a,b=b%i,(a+b)%i
            j=j+1
        print("fib数列对",i,"的余数数列的周期为",j-1)
        L.append(j-1)
    return L
m=remainder2(10000)
s=max(m)
print(s,m.index(s)+1)