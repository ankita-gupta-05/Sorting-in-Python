def selectionsort (arr):
	for i in range (0,len(arr)-1):
		mn = minimum (arr[i:])
		arr[i],arr[mn+i]=arr[mn+i],arr[i]
	return arr

def minimum (min_array):
	l = min_array[0]
	pos = 0
	for i in range (1,len(min_array)):
		if min_array[i]<l:
			l = min_array[i]
			pos = i
	return pos

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = selectionsort (a)
print a
