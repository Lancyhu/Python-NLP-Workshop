a = input("請輸入數字一: ")
a = int(a)
b = input("請輸入數字二: ")
b = int(b)
c = input("請輸入一個運算符號(+, -, *, /): ")
if c == "+":
    print("{}".format(a+b))

elif c == "-":
    print("{}".format(a-b))

elif c == "*":
    print("{}".format(a*b))

elif c == "/":
    print("{}".format(a//b))
else:
    print("not valid formula")
