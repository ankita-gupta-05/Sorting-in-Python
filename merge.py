def mergesort (arr):
	if len(arr)<=1:
		return arr

	middle =len(arr)/2
	left = arr[:middle]
	right = arr[middle:]
	left = mergesort (left)
	right = mergesort (right)
	return merge(left,right)

def merge (left,right):
	result = []
	l_index,r_index=0,0
	while l_index<len(left) and r_index<len(right):
		if left[l_index]<=right[r_index]:
			result.append(left[l_index])
			l_index+=1
		else:
			result.append(right[r_index])
			r_index+=1
	if left:
		result.extend(left[l_index:])
	if right:
		result.extend(right[r_index:])
	return result

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = mergesort (a)
print a
