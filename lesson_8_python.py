# Create class
class Car:
    brand = ""
    model_name = ""
    construction_year = 0

# Create objects of class
car1 = Car()

# Access attributes and assign new values
car1.brand = "Porsche"
car1.model_name = "Cayenne"
car1.construction_year = 2019

print(f"Brand: {car1.brand}, Model: {car1.model_name}, Year: {2019}")




# Define a class named Car with "__init__" function that initialises the attributes brand, model_name, and construction_year (Car class with constructor)
class Car:
    def __init__(self, brand, model_name, construction_year):
        self.brand = brand
        self.model_name = model_name
        self.construction_year = construction_year

    # The new return printable function
    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model_name}, Year: {self.construction_year}"
        
car1 = Car("Porsche", "Cayenne", 2019)    

print(car1)





## the new print version without commas as separator
#def __repr__(self):
        #return ("Brand: " + self.brand + " " + "Model: " + self.model_name + " " + "Year: " + str(self.construction_year))
