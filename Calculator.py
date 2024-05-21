#Calculator
# By working through this calculator code, you would have learned several key programming concepts:

# 1. **Defining Functions**:
#    - How to define basic functions in Python (`add`, `subtract`, `multiply`, `divide`) for arithmetic operations.

# 2. **Using Dictionaries**:
#    - How to map operation symbols to functions using a dictionary, enabling dynamic function calls.

# 3. **User Input**:
#    - Using `input()` to get user input and `int()` to convert input to integers.

# 4. **Iterating Over a Dictionary**:
#    - Displaying available operation symbols using a `for` loop to iterate over a dictionary.

# 5. **Dynamic Function Calls**:
#    - Retrieving and calling a function from a dictionary based on user input.

# 6. **String Formatting**:
#    - Using f-strings (`f"{num1} {operation_symbol} {num2} = {first_answer}"`) to format and print the calculation result.

# In summary, you learned to create a command-line calculator that takes user input, performs arithmetic operations, and displays the result using functions, dictionaries, loops, and string formatting in Python.

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)

#Here we select "+"
operation_symbol = input("Pick an operation: ") 
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
