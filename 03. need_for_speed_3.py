# First task from the lecture

def create_car(name, mileage, fuel):
    return {'name': name, 'mileage': mileage, 'fuel': fuel}

def drive(car, distance, required_fuel):
    if car['fuel'] >= required_fuel:
        car['mileage'] += distance
        car['fuel'] -= required_fuel
        print(f"{car['name']} driven for {distance} kilometers. {required_fuel} liters of fuel consumed.")
        
    else:
        print("Not enough fuel to make that ride")
        
    
    
    
def main_function():
    n = int(input())
    cars = []
    
    for _ in range(n):
        car_info = input().split('|')
        car = create_car(car_info[0], int(car_info[1]), int(car_info[2]))
        car.append(car)
   
    while True:
        command = input()
        
        if command == 'Stop':
            break
        
        tokens = command.split(' : ')
        action = tokens[0]
        car_name = tokens[1]
        
        
        for car in cars:
            if car['name'] == car_name:
                if action == 'Drive':
                    distance = int(tokens[2])
                    fuel = int(tokens[3])





print(f"Time to sell the {car}!")
print(f"{car} mileage decreased by {amount_reverted} kilometers")
print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


# Second task is from me

