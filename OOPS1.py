# Initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started Executing Data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attribute have been initiated")

    def travel(self, Destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {Destination}")

# Creating an Object/Instance of the Class
sam = employee()

# Printing the Attributes
# print(sam.id)

# Printina a method
sam.travel("Goa")

print(type(sam))