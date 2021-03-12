x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
li= sorted(num_list)
for i in range(len(num_list)):
    print(li[i])
