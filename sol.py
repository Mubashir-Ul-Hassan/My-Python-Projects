num1=int(input("Enter your first value:"))

num2=int(input("Enter your second value:"))
 
remainder=(num1 % num2);
modulus=(num1**num2);
divide=(num1/num2);
multiply=(num1*num2);
add=(num1+num2);
subtract=(num1-num2);


while True:
	
	choice=input("Enter the operator:(%,**,/,*,+,-):")
	if choice=="%":
		print(remainder);

	elif choice=="**":
		print(modulus);

	elif choice=="/":
		print(divide);

	elif choice=="*":
		print(multiply);

	elif choice=="+":
		print(add);

	elif choice=="-":
		print(subtract);

		break
		
	else:
		print("Invalid command");
	
	
