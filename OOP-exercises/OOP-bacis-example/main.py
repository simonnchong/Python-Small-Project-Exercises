class User:
    def __init__(self, user_id, user_name):
        print("New user has been created....")
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        
    
    def follow(self, user):
        self.following += 1 
        user.followers += 1

user_1 = User("001", "simon")
user_2 = User("002", "chong")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
