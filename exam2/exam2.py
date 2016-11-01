def binsearch(lst, target):
	if len(lst) == 0:
		return None
	idx = len(lst) // 2
	mid_value = lst[idx]
	if mid_value == target:
		return idx
	elif mid_value < target:
		tmp = binsearch(lst[idx+1:], target)
		if tmp != None:
			return idx + 1 + tmp
		return None
	else:
		return binsearch(lst[:idx], target)

def swap(lst, i, j):
	tmp = lst[i]
	lst[i] = lst[j]
	lst[j] = tmp

def rev(lst):
	mid = ( len(lst) + len(lst)%2 ) // 2
	for i in range(mid):
		swap(lst, i , len(lst) - i - 1)
	print(lst)

def main():
	a = []
	n = int(input())
	for _ in range(n):
		x = input()
		a.append(x)
	a.sort()
	print(a)
	while True:
		gg = input()
		print(binsearch(a, gg))


main()
