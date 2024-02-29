fibonacci_limit = int(input("Enter the Fibonacci limit :"))
xfirst = 0   
xlast = 1

print (xfirst)
print (xlast)
for i in range(0,fibonacci_limit):
    
    x = xfirst + xlast
    print(x)
    xfirst = xlast
    xlast = x
    