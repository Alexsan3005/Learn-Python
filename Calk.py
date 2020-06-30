x,oper,y=float(input("Введите первое число ")),input("Введите операцию "),float(input("Введите второе число "))
if oper == "+":
    print(x+y)
elif oper == "-":
    print(x-y)		
elif oper == "*":
    print(x*y)
elif oper == "pow":
    print(x**y)
elif oper == "/" and y == 0:
    print("Деление на 0!")
    y=float(input("Введите не 0:"))
    print(x/y)
elif oper == "/" and y != 0:
	  print(x/y)
if oper == "mod" and y == 0:
    print("Деление на 0!")
    y=float(input("Введите не 0:"))
    print(x%y)
elif oper == "mod" and y != 0:
	  print(x%y)
if oper == "div" and y == 0:
    print("Деление на 0!")
    y=float(input("Введите не 0:"))
    print(x//y)
elif oper == "div" and y != 0:
	  print(x//y) 
