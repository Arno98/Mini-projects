from time import sleep
def start_calc():
	print("Calculator is starting...")
	sleep(1)
	print("Calculator is ready for job!")
	print("You can enter next actions: '+' for adding, '-' for subtraction, '*' for multiplication, '/' for division, '**' for square.")
	print("Enter 'q' for exit.")
	while True:	
		f_n = float(int(input("Enter a number: ")))
		act = input("Enter an action: ")
		s_n = float(int(input("Enter a number: ")))
		if act == '+':
			print(f_n + s_n)
			continue
		if act == '-':
			print(f_n - s_n)
			continue
		if act == '*':
			print(f_n * s_n)
			continue
		if act == '/':
			print(f_n / s_n)
			continue
		if act == '**':
			print(f_n ** s_n)
			continue
		
start_calc()
