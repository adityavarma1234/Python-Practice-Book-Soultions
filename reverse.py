def main(filename):
	f = open(filename).readlines()
	for i in reversed(f):
		print i.strip()

if __name__ == "__main__":
	import sys
	main(sys.argv[1])

