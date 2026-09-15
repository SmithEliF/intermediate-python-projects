class User:

    def __init__(self, user_id, username):
#Self is the actual object being initialized

# Initializing Attributes
        self.id = user_id
        self.username = username

# Set attribute with default value
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "phil_pleeb")
user_2 = User("002", "eli_smith")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

# print(f"User {user_1.id}'s username is {user_1.username}")


