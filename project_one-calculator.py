print("""
+ ADD
- SUBSTRACT
* MULTIPLY
/ DIVISION
""")

val_1 = int(input("Enter your first value:- "))
val_2 = int(input("Enter your second value:- "))
opr = input("Enter your calculating operator:-")

if opr=="+":
    print(val_1+val_2)

elif opr=="-":
    print(val_1-val_2)

elif opr=="*":
    print(val_1*val_2)

elif opr=="/":
    print(val_1/val_2)

else:
    print("invalid operation")