try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ", result)
    print("Result is : ", result1)


except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    ("Please enter numerical value")
except NameError as ex:
    print("The exeption is ",ex)

except:
    print("some error occured")
finally:
    print("I will execute no matter what happens")

    
    
    