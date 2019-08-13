def func(*data):#一个*相当于元组
    for i in data:
        print(i,end=";")

func(1,2,3)

def log(**data):#两个**相当于字典
    for i in data:
        print(i,data[i])

log(x=2,y=3,z=4)
