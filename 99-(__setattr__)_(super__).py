"""1. What is __setattr__?
__setattr__ is a special (magic/dunder) method in Python that is called automatically whenever you assign a value to an instance variable.

Normal assignment:

python
Copy
Edit
obj.name = "joy"
is internally:

python
Copy
Edit
obj.__setattr__("name", "joy")
2. Default Behavior Without Override
If you don’t override __setattr__, Python’s default version simply puts the value into the object’s __dict__:

python
Copy
Edit
class A:
    pass

obj = A()
obj.name = "joy"  # stored in obj.__dict__
print(obj.__dict__)  # {'name': 'joy'}
3. Overriding __setattr__
You can intercept attribute assignments by defining __setattr__:

python
Copy
Edit
class A:
    def __setattr__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setattr__(key, value)  # actually store it

obj = A()
obj.name = "joy"
obj.age = 25
Output:

pgsql
Copy
Edit
Setting name to joy
Setting age to 25
4. Why Use super().__setattr__?
When you override __setattr__, you take full control of attribute assignment.
If you don’t call super().__setattr__, Python’s normal storage in __dict__ won’t happen — meaning the value won’t be saved.

Example (forgetting super()):

python
Copy
Edit
class A:
    def __setattr__(self, key, value):
        print(f"Tried to set {key} to {value}")

obj = A()
obj.name = "joy"
print(obj.__dict__)  # {}
The variable name isn’t stored anywhere.

5. Example: Read-Only Attribute
Here’s a real use-case — making name unchangeable after first assignment:

python
Copy
Edit
class Person:
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError(f"{key} is read-only")
        super().__setattr__(key, value)

p = Person()
p.name = "joy"    # works
p.name = "diya"   # error
6. Related Methods
__getattr__(self, key) → called when an attribute doesn’t exist.

__getattribute__(self, key) → called every time an attribute is accessed.

__delattr__(self, key) → called when an attribute is deleted.

✅ Learning Path:

Basics of Python OOP (class, self, __init__).

How objects store data in __dict__.

Special methods (__setattr__, __getattr__, __getattribute__, __delattr__).

super() and method resolution order (MRO).

Practical use cases (read-only attributes, validation, logging).

"""