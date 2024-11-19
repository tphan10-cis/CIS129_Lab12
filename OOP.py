#Thy Phan
#Lab 12
#18 November 2024

class Pet:
    def __init__(self, name="", type="", age=0):
        self.name = name
        self.type = type
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age


def main():
    animal = Pet()

    input_name = input("Enter a pet name: ")
    animal.set_name(input_name)

    input_type = input("Enter a pet type: ")
    animal.set_type(input_type)

    input_age = input("Enter a pet age: ")
    animal.set_age(input_age)

    print("\n")
    print(f"The pet name is: {animal.get_name()}")
    print(f"The pet type is: {animal.get_type()}")
    print(f"The pet age is: {animal.get_age()}")

if __name__ == "__main__":
    main()
