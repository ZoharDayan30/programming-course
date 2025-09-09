# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g= 9.8
    return h0-0.5 * g * t * t 
    # TODO: Implement this function
pass  # Replace with your code

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed= 20
    return speed * t 
   
def run_interactive ():
    h0= int(input("Enter initial height:"))
    t= int(input("Enter time:"))
    height= calculate_height(h0, t)
    print(f"Height of the ball at time {t} second{'s' if t != 1 else''} = {height:.1f} meters")

    t_car= int(input("Enter time for car (in seconds) : "))
    dist= calculate_car_distance(t_car)
    print(f"The car will travel {dist} meters in {t_car} second {'s' if t_car !=1 else ''}.")

run_interactive()
