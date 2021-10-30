from __future__ import print_function
import math

def print_halves(n):
	if n == 1:
		print(n)
		return n
	print_halves(int(n / 2))
	print(n)

def print_even_digits_from_right(n):
	if n == 0:
		return
	if (n % 10) % 2 == 0:
		print(n % 10)
	print_even_digits_from_right(n // 10)

def print_even_digits_from_left(n):
	if n == 0:
		return
	print_even_digits_from_left(n // 10)
	if (n % 10) % 2 == 0:
		print(n % 10)

def print_sequence(n):
	if n <= 1:
		print("1 ", end="")
		return
	if n == 2:
		print("1 1 ", end="")
		return
	if n % 2 == 0:
		print(str(n // 2) + " ", end="")
		print_sequence(n - 2)
		print(str(n // 2) + " ", end="")
	if n % 2 == 1:
		print(str(math.ceil(n / 2)) + " ", end="")
		print_sequence(n - 2)
		print(str(math.ceil(n / 2)) + " ", end="")

def main():
	print_halves(742)
	print_even_digits_from_right(291875614)
	print_even_digits_from_left(291875614)
	print_sequence(10)
	print()
	print_sequence(1)
	print()
	print_sequence(9)
	print()

main()

