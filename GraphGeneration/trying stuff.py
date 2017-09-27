

import itertools

iter = itertools.product('1234',repeat=10)
for i in range(0,1048576):
    comb = iter.next()
    print (comb)
    if comb == None:
        break
print ("end")
