# Assignment 1: Complex Conditions with Logical Operators

def check_conditions(a, b, c):
    if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c):
        print("Conditions met")
    else:
        print("Conditions not met")

# Example test cases
check_conditions(4, 2, 3)  # Conditions met
check_conditions(2, 2, 2)  # Conditions not met


# Assignment 2: Type Checking with Logical Operations

def validate_types(s, i, f):
    if isinstance(s, str) and isinstance(i, int) and isinstance(f, float):
        return "Valid input types"
    return "Invalid input types"

# Example test cases
print(validate_types("hello", 10, 3.5))  # Valid input types
print(validate_types(10, "hello", 3.5))  # Invalid input types
print(validate_types("test", 5, "3.5"))  # Invalid input types


# Assignment 3: Logical Operators with Boolean Values and Type Casting

def boolean_operations(x, y):
    x_bool = bool(x)
    y_bool = bool(y)
    print("x AND y:", x_bool and y_bool)
    print("x OR y:", x_bool or y_bool)
    print("NOT x:", not x_bool)
    print("x XOR y:", (x_bool and not y_bool) or (not x_bool and y_bool))

# Example test cases
print("Test Case 1:")
boolean_operations(1, "hello")  # True, True, False, False

print("\nTest Case 2:")
boolean_operations(0, None)  # False, False, True, False

print("\nTest Case 3:")
boolean_operations("", 5)  # False, True, True, True




