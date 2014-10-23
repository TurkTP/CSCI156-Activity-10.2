__author__ = 'Luke'
list=[69,1337,101,8008135,42,43,1]
for j in range(len(list)):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp
print(list)