#coding: utf-8
tmp = 10
if tmp<5:
    print "tmp<5"
elif tmp>10:
    print "tmp>10"
else:
    print "tmp == 10"

while tmp<13:
    tmp+=1
    print tmp

str = "abcd"
for index in str:
    print index,#不换行
for index in str:
    print index#换行
var = ""
for index in str:
    var += index
print var
