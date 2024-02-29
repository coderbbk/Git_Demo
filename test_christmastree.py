import time
start_time = time.time()

guess = int(input("Enter the number of christmas tree: "))

j = guess*2//2

for i in range(1,guess+1):
    x = 0
    z = 1
    spacestr = ""
    starstr = ""
    while (x <= j):
        spacestr = spacestr + " "
        x = x+1
    
    while (z <= 2*i-1):
        starstr = starstr+"*"
        z += 1
    print(spacestr+starstr+spacestr) 
    j = j-1   

print("--- %s seconds ---" % (time.time() - start_time))


    
    