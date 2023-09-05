color = ['red','white','green']
print("Original list:",color)
color = [v for elt in color for v in ('c',elt)]
print(color)