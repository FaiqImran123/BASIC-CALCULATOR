print("CALCULATOR")
funct =input("WANT TO PERFORM WHICH FUNCTION?")
a =int(input("ENTER FIRST NUMBER: "))
b =int(input("ENTER SECOND NUMBER: "))
if funct=="+":
    print("SUM IS", a+b)
elif funct=="-":
    print("SUB IS", a-b) 
elif funct=="*":
    print("MULTIPLY IS", a*b)
elif funct=="/":
    print("DIVISION IS", a/b)