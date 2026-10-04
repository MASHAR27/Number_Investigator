print("Keep entering numbers for the list , and if satisfied with the list , press zero to view the statistics")
numbers = []

while True:
    list_num = input("Enter the number for the list:  ").strip()
    if not list_num.isdigit():
        print("Please enter a number only ")
        continue
        
    list_num = int(list_num )
    if list_num  == 0:
        if len(numbers) == 0:
            print("Please have at least one number in the list before exiting ")
            continue
        else:
            break
    numbers.append(list_num)    
        
    
print(f"Your list = {numbers}")

# Firstly I want to create a unique values counter function
def unique_val(numbers):
    """ It will take a list of numbers and give the count of unique numbers in the list """
    unique = set()
    for num in numbers:
        unique.add(num) # I directly just add the numbers to the set since it will remove the duplicates automatically
        
    return len(unique)





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



            
        
    
    
def most_freq(numbers):
    """ Finds the most frequently occurring number in the list  """
    seen = {}
    
    for num in numbers:
        seen[num] = seen.get(num,0) + 1 # I increment the frequency as a value each time this number appears
        
    return max(seen,key = seen.get)    
 




def find_largest(numbers):
    """ Returns the largest number in the list """
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

       



def  find_smallest(numbers):
    """ Return the smallest number in the list  """
    smallest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
            
    return smallest
     




def  find_avg(numbers):
    """ Returns the average of the numbers in the list """
    
    total = 0
    for num in numbers:
        total += num
        
    return total/(len(numbers))








print("Number Investigator in Action:  ")
print("The number of unique values in the list:  ",unique_val(numbers))
print("These numbers are duplicates in the list:  ",num_of_duplicates(numbers))
print("The most frequent occurring number in the list: ",most_freq(numbers))
print("Largest number of the list:  ",find_largest(numbers))
print("Smallest number in the list: ",find_smallest(numbers))
print("Average of all the numbers in the list: ",find_avg(numbers))


