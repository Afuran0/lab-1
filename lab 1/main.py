def add (x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  if y==0:
    return "Error"
  else:
    return x/y
    def clear():
      return 0
def main():
  print("Simple calculator")
  print("Select operation:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Clear")
  print("6.Exit")

  
  
while True:
    choice=input("Enter choice (1/2/3/4/5/6):")

  if choice=="1":
    current_value=add(num1,num2)
  elif choice=="2":
    current_value=subtract(num1,num2)
  elif choice "3":
    current_value=multiply(num1,num2)
  elif choice=="4":
    current_value=divide(num1,num2)
print(f"Result:{current+value}")
elif choice=="5":
current_value=clear()
print("Calculator reset"):
elif choice=="6":
print("Exiting.")
break
else:
print("Invalid input... pls try again")
    
