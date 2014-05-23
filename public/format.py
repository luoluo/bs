import collections
f = open("foo1.txt")
line = f.readline().strip()
dicts = eval(line)
dicts = sorted(dicts.items())
#dicts = collections.OrderedDict(sorted(dicts.items()))
print "["
count = 0
for key in dicts:
    toPrint = "[\"%s\",%d]" % (key[0], key[1])
    if count+1 < len(dicts):
        toPrint = toPrint + ","
    count += 1
    print toPrint
print "]"
