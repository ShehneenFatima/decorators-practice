#upper-case decorators
def uppercase_decorators(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase_decorators
def greet(name):
   return f'Happy,{name}'
print(greet("Shehneen")) 
