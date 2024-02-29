 
s = "i am a good boy"
x = ""
s = s.strip()
print(s)
sl = s.split(' ')
sl = sl[::-1]
#print(type(sl))
for i in range(len(sl)):
    x = x + sl[i]+ " "
print(x)

