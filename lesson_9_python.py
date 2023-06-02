# Create a Vehicle class with max_speed and mileage instance attributes. 
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
       return f"The seating capacity of {self.name} is {capacity}."

##Testing
#modelZ = Vehicle("Model Z", 240, 20)
#print(modelZ.max_speed, modelZ.mileage)
#print(modelZ.seating_capacity(5))


# Create a Bus child class
class Bus(Vehicle):
    #new class attribute colour
    colour = "White"

    def seating_capacity(self, capacity=50):
       return super().seating_capacity(capacity)
    
coach = Bus("Model Y", 200, 30)
#print(coach.max_speed, coach.mileage)
print("Colour:", coach.colour, "Speed:", coach.max_speed, "Mileage:", coach.mileage)
print(coach.seating_capacity()) #default seat capacity
print(coach.seating_capacity(60)) #non-default capacity



#Bonus
# Create a Bus child class
class Bus(Vehicle):
    #new class attribute colour
    colour = "White"

    #new class attribute bus count
    count = 0

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        #increment the count when a new bus is created
        Bus.count += 1 
        #set the colour of all buses to red if at least 5 buses are created
        if Bus.count >= 5:
            Bus.colour = "Red"

    def seating_capacity(self, capacity=50):
       return super().seating_capacity(capacity)
    
coach1 = Bus("Model A", 200, 30)
coach2 = Bus("Model B", 180, 25)
coach3 = Bus("Model C", 220, 35)
coach4 = Bus("Model D", 240, 40)
coach5 = Bus("Model E", 220, 35)
#coach6 = Bus("Model F", 260, 45)

print(Bus.count)
print("Colour of coach1:", coach1.colour)
print("Colour of coach2:", coach2.colour)
print("Colour of coach3:", coach3.colour)
print("Colour of coach4:", coach4.colour)
print("Colour of coach5:", coach5.colour)
#print("Colour of coach6:", coach6.colour)



