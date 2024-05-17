def hello (name):
    print(f"Hello {name}")


def year_of_birth(name,age):
    year =2024-age
    print(f"Hello {name},you were born in {year}")

def my_country(country = "Uganda"):
    print(f"Hello Akirachix from {country}")


def greet(*names):
    for name in names:
        print(f"Hello {name}")

def create_sentence(**words):
    print(words)
    sentence=""
    for word in words.values():
        sentence +=word
        sentence +=""
    return sentence  
def sum_and_greet(*args,**kwargs):
    total = 0
    for x in args:
        total +=x
    f = kwargs["firstname"]
    l = kwargs["lastname"]
    greeting =f"Hello {f} {l} total of your numbers is {total}"
    return greeting

def find_unique_items(items_list):
    # Convert the list to a set to eliminate duplicates
    unique_set = set(items_list)
    
    # Initialize an empty list to store unique items
    unique_items = []
    
    # Iterate over the original list
    for item in items_list:
        # Check if the item is not in the set (i.e., it's unique)
        if item not in unique_set:
            unique_items.append(item)
    
    return unique_items

# Example usage
items_list = ["apple", "banana", "cherry", "apple", "banana"]
unique_items = find_unique_items(items_list)
print(unique_items)