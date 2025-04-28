#!/usr/bin/env python3
import argparse
import sys

def calculate(num1, operation, num2):
    """
    Perform calculation based on the provided operation and numbers.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":
        return num1 * num2
    elif operation == "div":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation.")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Basic command-line calculator")
    
    # Add arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operation", type=str, help="Operation to perform (add, sub, mul, div)")
    parser.add_argument("num2", type=float, help="Second number")
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Check if operation is valid
        if args.operation not in ["add", "sub", "mul", "div"]:
            print("Error: Invalid operation.")
            return
            
        # Perform calculation
        result = calculate(args.num1, args.operation, args.num2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()