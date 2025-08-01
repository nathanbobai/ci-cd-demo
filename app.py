import os

def hello():
    return "Hello, CI/CD!"

def dangerous_code():
    # Using eval() is a major security risk (arbitrary code execution)
    user_input = "print('This is unsafe!')"
    eval(user_input)  

if __name__ == "__main__":
    print(hello())
    dangerous_code()
