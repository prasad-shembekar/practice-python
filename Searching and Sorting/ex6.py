def insertionSort(list):
   for i in range(1,len(list)):

     curVal = list[i]
     pos = i

     while pos>0 and list[pos-1]>curVal:
         list[pos]=list[pos-1]
         pos = pos-1

     list[pos]=curVal

list = [14,46,43,27,57,41,45,21,70]
insertionSort(list)
print(list)
