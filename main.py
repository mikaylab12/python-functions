#Exercise 1 - Python Functions Powerpoint

#defining an argument
def distance_from_zero(number):
    if type(number) == int or type(number) == float:
        return abs(number)
    else:
        return "Nope"
#printing defined function:
print(distance_from_zero(6))
print(distance_from_zero(-5))
print(distance_from_zero(4.5))
print(distance_from_zero(-4.5))
print(distance_from_zero("What"))