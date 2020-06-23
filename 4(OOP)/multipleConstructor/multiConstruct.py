#more about init

class Hello:
    def __init__(self,name,age = 1):
        print("Hello from __init__")
        self.name = name
        self.age = age



usr1 = Hello('tripto', 22)
print(usr1.name, usr1.age)

