a=['mary', 'karuh','hbgd']
for i in range(len(a)):
    print(i,a[i])
list(range(5))
[0,0,12,12,21,12]

def fib(n):
    #Print Fibonacci Series.
    a,b=0,1
    while(a<n):
        print(a,end=" ")
        a,b=b,a+b
      
    print()

fib(200)