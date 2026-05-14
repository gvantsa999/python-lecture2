class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nUser Profile Summary:")
        print(f" Full Name: {self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back to your profile.")

user1 = User("mari", "Mtiulishvili", "mari_77", "mari@email.com", "Tbilisi")
user2 = User("Nia", "Kakhidze", "nia_k", "nia@email.com", "Telavi")
user3 = User("Erekle", "Megrelidze", "erekle_m", "erekle@email.com", "Zugdidi")
user4 = User("Gvantsa", "Beridze", "gvanca_b", "gvanca@email.com", "Tbilisi")
            
user1.describe_user()
user1.greet_user()
           
user2.describe_user()
user2.greet_user()
            
user3.describe_user()
user3.greet_user()
            
user4.describe_user()
user4.greet_user()