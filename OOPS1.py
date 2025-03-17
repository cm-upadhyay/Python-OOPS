# Initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print(id(self))
        # print("Started Executing Data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("Attribute have been initiated")

    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is now travelling to Delhi")

# Creating an Object/Instance of the Class
sam = employee()
sam.name = "Sam Kumar"
# print(id(sam))
print(sam.name)

# shaktiman = employee()
# print(id(shaktiman))

# Printing the Attributes
# print(sam.id)

# Printina a method
# sam.travel()

# print(type(sam))