numbers = [4, 7, 2, 7, 9, 4, 7, 2, 10, 9, 15, 4] # Just for testing  my code

# Firstly I want to create a unique values counter function
def unique_val(numbers):
    """ It will take a list of numbers and give the count of unique numbers in the list """
    unique = set()
    for num in numbers:
        unique.add(num) # I directly just add the numbers to the set since it will remove the duplicates automatically
        
    return len(unique)


print(unique_val(numbers))


