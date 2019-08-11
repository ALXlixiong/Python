
def ReadFile(handle):
    ret = "";
    for line in handle:
        ret += line
    return ret


handle = open("./txt.txt","r")
context = ReadFile(handle)
print context,
