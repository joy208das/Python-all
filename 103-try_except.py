class Animal:
    def __init__(self, name):
        self.name = name
      
    def did(self):
        try:
            result = self.name / 0
            print(result)
        except Exception as e:
            print("Error:", e)

a = Animal(25)
a.did()
