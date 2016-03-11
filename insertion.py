def insertionsort (arr):
	for i in range (1,len(arr)):
		j = i-1
		key=arr[i]
		while (arr[j]>key) and (j>=0):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
	return arr

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = insertionsort (a)
print a
