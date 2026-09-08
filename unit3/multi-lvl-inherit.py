#Multiple inheritance: Encryption + Authentication

class Encryption:
    def encrypt_data(self):
        print("Data is encrypted")

class Authentication:
    def verify_user(self):
        print("User authentication is performed")

class SecureData(Encryption, Authentication):
    def access_data(self):
        print("System provides secure data")


my_data = SecureData()
my_data.verify_user()
my_data.encrypt_data()
my_data.access_data()