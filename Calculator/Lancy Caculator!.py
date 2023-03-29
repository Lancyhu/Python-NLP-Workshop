x1 = int(input("please enter number one: "))
x2 = int(input("please enter number two: "))
op =input("please enter +,-,*,/: ") 

if op == "+":
    print(x1+x2)
elif op == "-":
    print(x1-x2)
elif op == "*":
    print(x1*x2)
elif op == "/":
    print("Quotient:{},Remainder:{}".format(x1//x2, x1 % x2))
else:
    print("Sorry,I can't answer.")


#給商數跟餘數在print地方用format