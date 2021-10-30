def sol(l, lst):
	lst.sort()
	dupes, rip = [], []
	counter, duplicate = 0, 0 
	for x in lst:
		if x == duplicate:
			counter += 1
			dupes.append(x)
		else:
			counter = 0
			duplicate = x
		if counter == 2:
			return 'No'
	for y in dupes:
		lst.remove(y)
	dupes.reverse()
	lst = list(map(str, lst))
	dupes = list(map(str, dupes))
	return 'Yes\n' + str(len(lst)) + '\n' + ' '.join(lst) + '\n' + str(len(dupes)) + '\n' + ' '.join(dupes)


def main():
	l  = int(input())
	lst = list(map(int, input().split()))
	print(sol(l, lst))


main()


