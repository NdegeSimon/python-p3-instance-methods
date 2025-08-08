class Person:
    def walk(self):
        print("The person is walking.")  # Changed from "The person is walking!"
    
    def talk(self):
        print("Hello World!")
    
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        self.talk()
        self.walk()