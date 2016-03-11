def bubblesort (arr):
	changed = True
	while changed:
		changed = False
		for i in range (len(arr)-1):
			if arr[i]>arr[i+1]:
				arr[i],arr[i+1]=arr[i+1],arr[i]
				changed = True
	return arr

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = bubblesort (a)
print a
