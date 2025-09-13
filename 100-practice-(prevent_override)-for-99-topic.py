"""can not overload or override"""

class dong:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.name = "doya"  - you can not do this
        self.age = 22
        self.age = 20

    def __setattr__(self, key, value):
        # If the attribute already exists, block changing it
        if key== 'name' and key in self.__dict__:
            raise AttributeError(f"Can't modify '{key}', it is read-only")
        super().__setattr__(key, value)

    def display(self):
        print(self.name, self.age)

a = dong("joy", 25)
a.display()


""" In your code:

if key in self.__dict__: → Checks if the attribute already exists.

raise AttributeError(...) → Stops the program and says “you can’t change this.”

super().__setattr__(key, value) → Actually sets the attribute if allowed.

"""

