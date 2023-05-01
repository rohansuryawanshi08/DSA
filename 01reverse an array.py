def reverse_list(l):
    s=0
    e=len(l)-1
    while s<e:
        l[s],l[e]=l[e],l[s]
        s=s+1
        e=e-1
        
        
 # method 2
l=[10,20,30]
l3=l[::-1]
print(l3)
