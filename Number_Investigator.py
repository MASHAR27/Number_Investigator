numbers = [4, 7, 2, 7, 9, 4, 7, 2, 10, 9, 15, 4] # Just for testing  my code

# Firstly I want to create a unique values counter function
def unique_val(numbers):
    """ It will take a list of numbers and give the count of unique numbers in the list """
    unique = set()
    for num in numbers:
        unique.add(num) # I directly just add the numbers to the set since it will remove the duplicates automatically
        
    return len(unique)


print(unique_val(numbers))


def num_of_duplicates(numbers):
    """ To return the numbers which are duplicates in the list """
    
    duplicates = set()
    seen = []
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.append(num)
            
    return duplicates


print(num_of_duplicates(numbers))
            
        
    
    
def most_freq(numbers):
    """ Finds the most frequently occurring number in the list  """
    seen = {}
    
    for num in numbers:
        seen[num] = seen.get(num,0) + 1 # I increment the frequency as a value each time this number appears
        
    return max(seen,key = seen.get)    
 

print(most_freq(numbers))