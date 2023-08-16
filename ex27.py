# Write a Python program to find the type of the progression

def ap_gp(arr):
    if arr[0]==arr[1]==arr[2]==0:
        return "Wrong NUmbers"
    else:
        if arr[1]-arr[0]==arr[2]-arr[1]:
            n=2*arr[2]-arr[1]
            return "AP Seq & next number is "+str(n)
        else:
            n = arr[2]**2/arr[1]
            return "Gp seq & next number is "+str(n)
        
print(ap_gp([1,2,3]))