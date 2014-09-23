import random

def print_to_file(f, no):
	#print("print_to_file")
	x = random.randint(0, 9)
	y = random.randint(0, 9)
	op = random.randint(0, 1)
	op_str = "+"
	if op == 0 and x>=y:
		op_str = "-"
	f.write("({0:3d}) {1} {2} {3} =      ".format(no, str(x), op_str, str(y)))

def main():
	x = 4
	y = 25
	z = 10
	f = open("output.txt","w") 
	for k in range(z):
		f.write("[{0}]###########################################################\n"\
			.format(k))
		for j in range(y):
			for i in range(x):
				print_to_file(f, (i+1)*(j+1))
			f.write("\n")
	f.close()
#	with open("output.txt") as f:
#		for line in f:
#		    print line

if __name__ == "__main__":
    main()
