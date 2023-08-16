# Write a Python program that compute the area of the polygon . The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections.

def poly_area(c):
    add = []
    for i in range(0,(len(c)-2),2):
        add.append(c[i]*c[i+3]-c[i+1]*c[i+2])
        add.append(c[len(c) - 2]*c[1]-c[len(c)-1]*c[0])
        return abs(sum(add)/2)

no_sides = int(input("Input number of sides:"))
cord_data = []
for z in range(no_sides):
    print("Side:",z+1)
    print("Input co-ordinates:")
    x = int(input("Enter x val"))
    y = int(input("Enter y val:"))
    cord_data.append(x)
    cord_data.append(y)
print("Area of polygon:",poly_area(cord_data))

