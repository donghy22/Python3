class MyClass:

    def info(self):
        print("name : ", self.name)
        print("university : ", self.university)
        print("major : ", self.major)
        print("email : ", self. email)

    def set_info(self):
        self.name=input("name : ")
        self.university=input("university : ")
        self.major=input("major : ")
        self.email=input("email : ")

MyClass1=MyClass()
MyClass1.set_info()

print()
MyClass1.info()







