def main():
    # Get two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate sum, difference, product, and quotient
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    if num2 != 0:
        quotient = num1 / num2
    else:
        quotient = "undefined (division by zero)"
    
    # Print the results
    print("Sum: ", sum_result)
    print("Difference: ", difference)
    print("Product: ", product)
    print("Quotient: ", quotient)

if __name__ == "__main__":
    main()
