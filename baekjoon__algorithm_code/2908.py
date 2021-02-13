x=input()
x,y=x.split(' ')

x_list=list(x)
y_list=list(y)
x_list.reverse()
y_list.reverse()
x=int(''.join(x_list))
y=int(''.join(y_list))
if x>y:
    print(x)
else:
    print(y)
