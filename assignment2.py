while True:
    try:
        # Get first number
        num1 = float(input("Enter the first number: "))
        
        # Get second number
        num2 = float(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        
        # Display result
        print(f"Result: {num1} / {num2} = {result}")
        break  # Exit loop if successful
        
    except ValueError:
        print("Error: Please enter valid numbers only.")
        print("Try again.\n")
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        print("Try again.\n")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Try again.\n")