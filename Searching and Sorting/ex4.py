# bubble sort

def bubble(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
            
list = [14,46,43,27,57,41,45,21,70]
bubble(list)
print(list)