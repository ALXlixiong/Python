#coding:utf-8
import random

def GetRandomNum(low,high):
    return random.randint(low,high)

low = input("请输入随机数下限:")
high = input("请输入随机数上限:")

ans = GetRandomNum(low,high)

tmp = input("请输入答案:")

while True:
    if int(tmp) == ans:
        print "恭喜你猜对了",tmp
        break
    elif int(tmp)>ans:
        print "猜大了"
        tmp =input("请输入答案:")
    else:
        print "猜小了"
        tmp =input("请输入答案:")
print "end..."
