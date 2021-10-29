def indent(n):
	return (" " * n)

def is_true(s):
	return (s.replace(" ", "").find("true") > -1)

def contains_rep(s, t):
	return (s.find(t) > -1)

def shift_char(ch, n):
	value = ord(ch)
	value = value + n
	if value > 122:
		value = value - 25
		return chr(value)
	else:
		return chr(value)

def average_ch(s):
	counter = len(s)
	value = 0
	for x in range(0, counter):
		value = value + ord(s[x])
	return chr(value // counter)

def mixed_case(s):
	ans = ""
	counter = len(s)
	for x in range(0, counter):
		if x%2==0:
			ans = ans + s[x:x+1].lower()
		else:
			ans = ans + s[x:x+1].capitalize()
	return ans	

def occurrences(s, t):
	first_index = 0
	counter = 0
	x = 0
	while x < len(s):
		if s[x:x + len(t)].find(t) > -1:
			counter = counter + 1
		x = x + 1
	return counter

def sum_numbers(s):
	s.replace(" ", "")
	ans = 0
	for x in range(0, len(s)):
		if s[x:x+1].isdigit():
			ans = ans + int(s[x:x+1])
	return ans

def intersperse(s, t):
	ans = ""
	for x in range(0, len(s)):
		if x < len(s) - 1:
			ans = ans + s[x:x+1] + t
		else:
			ans = ans + s[x:x+1]
	return ans

def swap_at(s, n):
	first_part = s[0:n]
	second_part = s[n:]
	return second_part + first_part

def evaluate(s):
	subtract = "-"
	add = "+"
	ans = int(s[0:1])
	for x in range(1, len(s)):
		if s[x:x+1] in add:
			ans = ans + int(s[x+1:x+2])
			x = x + 1
		elif s[x:x+1] in subtract:
			ans = ans - int(s[x+1:x+2])
			x = x + 1
	return ans


def main():
	print(indent(4))
	print(is_true("t r ue"))
	print(contains_rep("heyheyhey", "hey"))
	print(shift_char('c', 5))
	print(average_ch("hello"))
	print(mixed_case("Hello world!"))
	print(occurrences('aaaaa', 'aa'))
	print(sum_numbers("hey 1232    4h"))
	print(intersperse('hello world', '-'))
	print(swap_at('hello world!', 5))
	print(evaluate("6+9+3-4-6"))


main()
