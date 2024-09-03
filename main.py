# Solution 1: Add Two Numbers
def add_numbers(num1, num2):
    
    # This function takes two numbers and returns their sum.
    return num1 + num2
result = add_numbers(3, 7)

print(result)  


# Solution 2: Check if Number is Even
def is_even(num):
    
   # This function returns True if the number is even, and False otherwise.
    return num % 2 == 0

print(is_even(5))  


# Solution 3: Reverse a String
def reverse_string(text):
    
    # This function returns the reversed version of the input string.
    return text[::-1]

print(reverse_string("python")) 


# Solution 4: Count Vowels in a String
def count_vowels(text):
    
    #This function returns the count of vowels (a, e, i, o, u) in the string.
    vowels = 'aeiou'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("programming")) 


# Solution 5: Calculate Factorial of a Number
def calculate_factorial(n):
    
    # This function calculates the factorial of a non-negative integer n.
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(calculate_factorial(4)) 


# Solution 6: Apply a Decorator to a Function
def apply_decorator(func):
    
    # This function applies a decorator to the given function.
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

# Example usage of the decorator
@apply_decorator
def sample_function():
    return "Function executed"

print(sample_function())  


# Solution 7: Sort List of Tuples by Age
def sort_by_age(people):
    
    # Sorts a list of tuples by age in ascending order.
    return sorted(people, key=lambda x: x[1])

# Example usage:
people = [("Ian", 20), ("David", 25), ("Peter", 35), ("Justin", 28)]
sorted_people = sort_by_age(people)
print(sorted_people) 


# Solution 8: Merge Two Dictionaries
def merge_dicts(dict1, dict2):
  
    # Merges two dictionaries. If a key exists in both, their values are summed up.
    merged_dict = dict1.copy()  # Start with all items from dict1
    for key in dict2:
        merged_dict[key] = merged_dict.get(key, 0) + dict2[key]
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2)) 


# Solution 9: Car Class
class Car:
  
    # Class representing a car with make, model, and year attributes.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_information(self):
     
    # Print out the car's information.
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Example usage of the Car class
my_car = Car("Mercedes", "GLE 450d", 2022)
my_car.display_information() 

