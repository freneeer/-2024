f = open('27a.txt')
a = list(map(int,f))
s =  0
count = 0
f = 0
for i in range(0,len(a)):
    s += a[i]
    f+=1
    if f % 7 == 0:
        if s > 12:
            count+=1
        s = 0
            
   
print(count)