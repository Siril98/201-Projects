# Testing page for homework 6 functions:

integer_list = []
SENTINEL = 0
def summation():
    
    integer_list = []
    SENTINEL = 0
    
    value = int(input("Please enter a number, 0 to stop:"))
    integer_list.append(value)
    while value != SENTINEL:
        print(value)
        value = int(input("Please enter a number, 0 to stop:"))
        integer_list.append(value)
    else:
        integer_list.remove(SENTINEL)
    print("For the list",integer_list)
        
    for i in integer_list:
        summation = sum(integer_list)
    print("The summation is:" ,summation)    


def multiply():

    for m in integer_list:
        product = sum(integer_list)
        print("The product is:",product)

summation()
multiply()




    
