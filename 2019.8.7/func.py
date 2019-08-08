def add(x,y):
    return x+y
def func(flag = False):
    if flag:
        print "true"
    else:
        print "false"

print(add(1,2))
func()
func(True)

def GetResult():
    return 1,2,3
x,y,z = GetResult();
print x,y,z
Func = GetResult;
_,y,_ = Func();
print y

print type(Func)
