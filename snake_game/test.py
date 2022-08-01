l=[]
h=[]

for i in range (0,10):
    h=[]
    h.append(i)
    h.append(i+1)
    l.append(h)
    if len(l)>2:
       del l[0]

    # print(h)
    print(l)

# for i in range (0,2):
#     l.append(h)
#     print(l)