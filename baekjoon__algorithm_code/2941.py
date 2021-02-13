cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
x=input()

for i in cro:
    if i in x:
        x=x.replace(i," ")
        
print(len(x))
