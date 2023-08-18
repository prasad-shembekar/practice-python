def selection(list):
    for i in range(len(list)-1,0,-1):
        maxpos = 0
        for j in range(1,i+1):
            if list[j] > list[maxpos]:
                maxpos = j

        list[i] , list[maxpos] = list[maxpos],list[i]
        

list = [14,46,43,27,57,41,45,21,70]
selection(list)
print(list)