
def GetLineWordCount(handle):
    dict = {}
    for line in handle:
        if line[:-1] not in dict:
            dict[line[:-1]] = 1
        else:
            dict[line[:-1]] += 1
    return dict

handle = open("./txt.txt","r")

dict = GetLineWordCount(handle)
print dict,

handle.close()
