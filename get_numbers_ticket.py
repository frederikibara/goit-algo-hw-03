import random

def get_numbers_ticket(min, max, quantity) -> list:    
    """
    "Function generate random numbers and return list of unique numbers within specified parameters."
    """
    numbers = set()
    
    if (min < 0 or max > 1000 or quantity > max):
        return list(numbers)
        
    while quantity != len(numbers):
        numbers.add(random.randint(min, max))
        
    sorted_list = sorted(list(numbers))
    return sorted_list
             
    
print(get_numbers_ticket(1, 10, 3))



