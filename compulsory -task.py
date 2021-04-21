# Compulsory Python Function Task
# defining cost of the hotel per night
def hotel_cost(nights):
    return nights*140

# defining cost of the plane ride
def plane_ride_cost(city):
    if "CPT" == city:
        return 2500
    elif "DBN" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BFN" == city:
        return 1800
    else:
        return "The location not in our database"

# defining the cost of a rental car
def rental_car_costs(days):
    car_cost= 40 * days # cost is in rands

    if days >= 7:
        car_cost = car_cost - 50
    elif days >= 3 and days < 7: # cannot receive both discounts
        car_cost = car_cost - 20
    return car_cost

# defining the cost of the trip
def trip_cost(city, days, spending_money):
    return rental_car_costs(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

location = input("Where did you go: ")
days = int(input("How many days did you stay: "))
extras = float(input("How much did you spend on extras: "))

print(trip_cost(location, days, extras))


