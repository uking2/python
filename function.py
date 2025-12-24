# #function is set of statements that performs a specific task.
# # def cal(a, b):#function definition
# #     sum = a + b  #function body
# #     print("Sum is:", sum) #function body
# #     return sum #return statement

# # cal(5, 10) #function call



# def caL(a,b): #function definition # a,b are parameters
#     return a + b

# sum =caL(5,10) #function call
# print("Sum is:", sum) 


# def print_hello():
#     print("helloo world")

# print_hello()
# print_hello()    


# def average(a,b,c):
#     return (a+b+c) /3

# avg =average(4,7,9)
# print("avrage of 3 numbers is:", avg)


#q1 waf to print the lenghth of list

nums =["ahm","mumbai","delhi","goa"]

def print_length(lst):
    return len(lst)

length = print_length(nums)
print ("Length of the list is:", length)

##q2 factorial of number using function


def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    return fact

num = factorial(5)
print("Factorial is:", num)      