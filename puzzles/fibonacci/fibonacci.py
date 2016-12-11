# fibonacci.py
import sys

def fibonacci_n(n):
	'''Return the nth Fibonacci number starting from 0
	e.g. fibonacci_n(8) ==> 13
	'''
	a,b = 0,1
	for i in range(n):
		a,b = b, a+b

	return a

def fibonacci_n_less(n):
	'''Return the largest fibonacci number less than n
	e.g. fibonacci_n_less(10) ==> 8
	'''
	a,b, = 0,1
	while b < n:
		a,b = b,a+b

	return a

def fibonacci_n_recursive(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci_n_recursive(n-1) + fibonacci_n_recursive(n-2)

def fibonacci_n_less_recursive(n):
	if n == 0 or n == 1:
		return 0
	


if __name__ == '__main__':
	# print [fibonacci_n(x) for x in range(15)]
	# print [fibonacci_n_less(x) for x in range(15)]
	if len(sys.argv) > 1:
		print fibonacci_n_recursive(int(sys.argv[1]))
