


# Testing Recursions



def recursion(height,count):

    
    count+=1
    print("count is:",count)
    
    if height < 1 :
        return("Invalid height of", height)
    if height % 2 == 0:
        print(height)
        height = height / 2
        return recursion(height,count)
    if height == 1:
        return "Height of",height
    if height % 2 != 0:
        print(height)
        height = height*3+1
        return recursion(height,count)
    
def main():
    count = 0
    print("Welcome")

    height = int(input("Please enter height:"))
    bob = recursion(height,count)
    print(bob)
    
main()
