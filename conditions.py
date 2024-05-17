def print_numbers(n):
    numbers= range(n)
    for number in numbers:
        print(number)

def print_even_numbers(n):
    numbers= range(n)
    for number in numbers:
        if number %2 ==0:
         print(number)


def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number %2 ==0:
            print(f ("{number} is even"))
        else:
            print(f"{number} is odd")

     
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number %2 == 0:
         print(f"{number} is divisible by 2")
        elif number %3 ==0:
         print(f"{number} is divisible by 3")
        elif number %5 ==0:
         print(f"{number} is divible by 5")
        elif number %7 ==0:
         print (f"{number} is divisible by 7")
        else:
         print (f"{number} is not divisible")
    
def count_down(n):
    while n>0:
        print(n)
        n -=1

def countdown_to_five(n):
    while n> 0:
        print(n)
        if n ==5:
            break
        n-=1

def divisible_by_sum(n):
    x=1
    while x<=n:
        x+=1
        if x% 7!=0:
            continue
        print (x)

def fizzbuzz(n):
    numbers = range(n)
    for number in numbers:
        if number %3 ==0:
            print(f"fizz")
        elif number %5 ==0:
            print(f"Buzz")
        else:
            print(f"FizzBuzz")   


def print_even_numbers():
    number = 0
    while number <= 50:
        if number % 2!= 0:  
           number += 1
           continue  
        print(number)  
        number += 2







    
    