import operator 
d = {1:2,3:4,4:3,2:1,0:0}
print("Original dictionary:",d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1))
print("Ascending order dictionary:",sorted_d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order:",sorted_d)
