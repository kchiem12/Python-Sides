def ones_digits(l):
	l2 = []
	for x in range(0, len(l)):
		l2.append(l[x] % 10)
	return l2

def lengths_of(l):
	l2 = []
	for x in range(0, len(l)):
		l2.append(len(l[x]))
	return l2

def filter_odd_lengths(l):
	l2 = []
	x = 0
	while x < len(l):
		if not len(l[x]) % 2 == 0:
			l2.append(l[x])
		x = x + 1
	return l2

def filter_upper(l):
	l2 = []
	x = 0
	while x < len(l):
		if l[x].isupper():
			l2.append(l[x])
		x = x + 1
	return l2

def list_all(l):
	if len(l) == 0:
		return False
	for x in range(0, len(l)):
		if not l[x]:
			return False
	return True

def list_any(l):
	for x in range(0, len(l)):
		if l[x]:
			return True
	return False

def immutable_replicate(l, n):
	l2 = []
	l2 = l*n
	return l2

def mutable_replicate(l, n):
	l.extend(l*(n - 1))

def at_least(l, s, n):
	counter = l.count(s)
	if counter >= n:
		return True
	return False




def main():
	immutable_list = ['Hey', 'Whatup']
	mutable_list = ['DaBaby', 'Lewis Capaldi']

	print(ones_digits([321, 49120, 9112]))
	print(lengths_of(['hello', 'world', '!']))
	print(filter_odd_lengths(['heyo', 'library', 'no', 'money']))
	print(filter_upper(['HEY', 'No', 'pole', 'YOLO']))
	print(list_all([True, True, False]))
	print(list_any([True, True, False, True]))
	print(immutable_replicate(immutable_list, 4))
	print(immutable_list)
	mutable_replicate(mutable_list, 3)
	print(mutable_list)
	print(at_least(['Heyo', 'Heyo', 'heyo'], 'heyo', 1))



main()