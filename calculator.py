# Calculator

def add(x,y):
   return x+y
def subtract(x,y):
   return x-y
def multiply(x,y):
   return x*y
def divide(x,y):
   if y!=0:
     return x/y
   print("error! divide by 0")

print("select opertor")
print("add")
print("subtract")
print("multiply")
print("divide")
choice = input("enter a opertor : ")

num1 = float(input("enter a number :"))
num2 = float(input("enter a number :"))

if choice == '+':
   print(f"the rueslt is : {add(num1,num2)}")
elif choice == '-':
   print(f"the rueslt is : {subtract(num1,num2)}")
elif choice == '*':
   print(f"the rueslt is : {multiply(num1,num2)}")
elif choice == '/':
   print(f"the rueslt is : {divide(num1,num2)}")
else:
   print("invalid number")

