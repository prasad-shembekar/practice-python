# Number in a Matrix: Maximum in its column and minimum in its row.
def matrix_number(matrix):
   result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
   return list(result)
m1 = [[1,2], [2,3]]
print("Original matrix:",m1)
print("Number in the said matrix which is maximum in its column and minimum in its row:")
print(matrix_number(m1))
m1 = [[1,2,3], [3,4,5]]
print("\nOriginal matrix:",m1)
print("Number in the said matrix which is maximum in its column and minimum in its row:")
print(matrix_number(m1))
m1 = [[7,5,6], [3,4,4], [6,5,7]]
print("\nOriginal matrix:",m1)
print("Number in the said matrix which is maximum in its column and minimum in its row:")
print(matrix_number(m1))

