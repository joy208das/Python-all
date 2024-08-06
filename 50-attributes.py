class User:

    def __init__(self, user_id, user_name):          #attributes
        self.id = user_id
        self.username = user_name



user_1 = User("001", "joy")

print(user_1.id)
print(user_1.username)

user_2 = User("002", "diya")


# user_2 = User()
# user_2.id = "002"
# user_2.name = "diya"