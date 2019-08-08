handle = open("./txt.txt","r")
ret = {}
for line in handle:
    line = line[:-1]
    if line not in ret:
        ret[line] = 1
    else:
        ret[line] += 1
print ret
handle.close()
