f = open('17.txt')
nomer = 0
spisokrazn = []
for i in f:
    a = i.split()
    a = list(map(int,a))
    nomer  +=1
    if nomer % 2 == 0:
        razn = a[0] - a[-1]
        spisokrazn.append(razn)
    else:
        razn = a[-1] - a[0]
        spisokrazn.append(razn)
print(max(spisokrazn),min(spisokrazn))
        
        