from collections import namedtuple

# Define the Car namedtuple
Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])

# Create two car objects
car1 = Car(make='Toyota', model='Camry', price=24000, horsepower=203, seats=5)
car2 = Car(make='Honda', model='Civic', price=22000, horsepower=158, seats=5)

# Calculate the sum of the price of both cars
total_price = car1.price + car2.price

print(f"The total price of both cars is: ${total_price}")
