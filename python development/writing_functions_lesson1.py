#FUNCTIONS: DEF
#FUNDAMENTAL WAY TO STRUCTURE CODE
'''
def greet(name):
    print(f"Hello😊, {name}")
    
greet("Phema")

def add(a, b):
    return a + b

result = add(2, 10)
print(result)
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) #RECURSION
    
def greet(name, greeting= "Hello"):
    print(f"{greeting}, {name}")
    
greet("Mmakaphema😊🤸", "Good morning sana😍😻")