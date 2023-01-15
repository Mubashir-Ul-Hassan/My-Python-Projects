
num1=int(input("Enter your first value:"))
choice=input("Enter the operator:(%,**,/,*,+,-):")
num2=int(input("Enter your second value:"))
 
remainder=(num1 % num2);
modulus=(num1**num2);
divide=(num1/num2);
multiply=(num1*num2);
add=(num1+num2);
subtract=(num1-num2);


if choice=="%":
	print("Your remainder is:", remainder);

elif choice=="**":
	print("Your modulus is:", modulus);

elif choice=="/":
	print("Your divition is:", divide);

elif choice=="*":
	print("Your multiplication is:", multiply);

elif choice=="+":
	print("Your addition is:", add);

elif choice=="-":
	print("Your subtraction is:", subtract);

else:
	print("Invalid command");
