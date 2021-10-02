# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result1 = [[0,0,0],
         [0,0,0]]
result23 = [[0,0,0],
         [0,0,0]]
result45 = [[0,0,0],
         [0,0,0]]
result5 = [[0,0,0],
         [0,0,0]]
result6 = [[0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


for i in range(len(y)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for rs in result:
   print(rs)
for is in range(len(z)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for rss in result:
   print(rss)
   
  
  
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
	print ("%d" %arr[i]),
# This code is contributed by Mohit Kumra

   
  # Python program to find the
# difference between two times


# function to obtain the time
# in minutes form
def difference(h1, m1, h2, m2):
	
	# convert h1 : m1 into
	# minutes
	t1 = h1 * 60 + m1
	
	# convert h2 : m2 into
	# minutes
	t2 = h2 * 60 + m2
	
	if (t1 == t2):
		print("Both are same times")
		return
	else:
		
		# calculating the difference
		diff = t2-t1
		
	# calculating hours from
	# difference
	h = (int(diff / 60)) % 24
	
	# calculating minutes from
	# difference
	m = diff % 60

	print(h, ":", m)

# Driver's code
if __name__ == "__main__":
	
	difference(7, 20, 9, 45)
	difference(15, 23, 18, 54)
	difference(16, 20, 16, 20)

# This code is contributed by 

  
