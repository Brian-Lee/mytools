#nice snippet to remember
# c = {'a':10, 'b':1, 'c':22}
# print( sorted( [ (v, k) for k,v in c.items() ] ) )
#[(1,'b'), (10, 'a'), (22,'c')]


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = []
for line in handle:
    
    if 'From ' not in line:
        continue
    hour = line.strip().split()[5].split(':')[0]
    #print(hour)
    
    hours.append(hour)
    
#print(hours)
hours_hist = dict()
for h in hours:
    hours_hist[h] = hours_hist.get(h,0) + 1
    
sorted_list = []
for k, v in hours_hist.items():
    #print(k,v)
    temptpl = (k,v)
    #print(temptpl)
    sorted_list.append(temptpl)
'''	
nsorted_list = []
for v, k in sorted_list(sorted_list.items()):
    #print(k,v)
    temptpl = (k,v)
    #print(temptpl)
    nsorted_list.append(temptpl)
 '''   


#print(sorted_list)
sorted_list = sorted(sorted_list)


#print(sorted_list)
for k, v in sorted_list:
    print(k, v)
	