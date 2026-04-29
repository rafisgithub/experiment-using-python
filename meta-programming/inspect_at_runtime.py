class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, I'm {self.name}"

user = User("Alice", 30)

# Inspect attributes
print(hasattr(user, 'name'))           # True
print(getattr(user, 'name'))           # "Alice"
setattr(user, 'email', 'alice@example.com')
print(dir(user))                       # Shows all attributes/methods

# Get type information
print(type(user))                      # <class '__main__.User'>
print(user.__class__.__name__)         # "User"