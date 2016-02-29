def main(filename):
	f = open(filename).readlines()
	for i in f:
		print i.strip()[::-1]
