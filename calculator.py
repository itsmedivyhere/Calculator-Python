#calculator

print("hello I'm A mini Calculator")
a=int(input("enter the value:"))
b=int(input("enter the value:"))

print("please select the choice")
print("Choose 1 for Add")
print("Choose 2 for Sub")
print("Choose 3 for Divide")
print("Choose 4 for Multiply")

ch=int(input("enter the choice:"))

if (ch==1):
    print('Addition of the given Values:',a+b)
elif (ch==2):
    print('Subtraction of the given Values:',a-b)
elif (ch==3):
    print('Division of the given Values:',a/b)
elif (ch==4):
    print('Multiplication of the given Values:',a*b)
else:
    print("Alert:Select the valid choice please")
