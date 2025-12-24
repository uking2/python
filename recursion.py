# recursion function call itself

def show(n):
    if n==0: #base case
        return
    print(n)
    show(n-1) # recursive call

show(5) # Output: 5 4 3 2 1


      