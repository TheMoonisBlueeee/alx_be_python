number1=input("Enter the first number:")
number2=input("Enter the second number:")
operation=input("Choose an operation (+,-,*,/):")

def result (number1,number2,operation):
  match operation:
    case "+":
        return number1+number2
    
    case "-":
           return number1-number2
    
    case "*":
          return number1*number2

    case "/":
          if number2==0:
               print("Cannot divide by zero")
               return number1/number2
