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

def print_to_file_add_20(f, no):
	print_to_file_20(f, no, 1)

def print_to_file_sub_20(f, no):
	print_to_file_20(f, no, 0)

def print_to_file_both_20(f, no):
	print_to_file_20(f, no, -1)

def print_to_file_20(f, no, op_input):
	while True:

		x = random.randint(10, 19)
		y = random.randint(2, 9)	
	
		if op_input < 0 or op_input > 1:
			op = random.randint(0, 1)

		difficult = no % 2 
		if 0 == difficult:
			x = random.randint(15, 19)
			y = random.randint(6, 9)
			print "{0} {1} {2}".format(x, "+" if op==1 else "-", y)

		op_str = "+"
		if 0 == op and x - y > 0:
			op_str = "-"
			f.write("({0:3d}) {1:2d} {2} {3:2d} =      ".format(no, x, op_str, y))
			break;
		if 1 == op and x + y <=19 and x + y >=10:
			f.write("({0:3d}) {1:2d} {2} {3:2d} =      ".format(no, x, op_str, y))
			break;

def main():
	x = 4
	y = 20
	z = 1
	f = open("output.txt","w") 
	for k in range(z):
		f.write("[{0}]###########################################################\n"\
			.format(k))
		for j in range(y):
			for i in range(x):
				#print_to_file_add_20(f, (i+1)+ 4*j)
                                #print_to_file_sub_20(f, (i+1)+ 4*j)
				print_to_file_both_20(f, (i+1)+ 4*j)
			f.write("\n")
	f.close()
#	with open("output.txt") as f:
#		for line in f:
#		    print line

if __name__ == "__main__":
    main()
