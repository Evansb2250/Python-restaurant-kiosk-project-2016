acceleration = 9.8
initialSpeed = 10
time = 4


def distance_traveled(distance):
    if(distance > 100):
        print("distance traveled = ", distance, "\nGood going")
    elif(distance < 50):
        print("distance traveled = ", distance, "\nPathetic")
    else:
        print("distance traveled = ", distance, "\nnot bad")




distance_traveled(distance = (initialSpeed * time) + (0.5 * (acceleration * (time * time))))






initialSpeed = 0
time = 2
distance_traveled(distance = (initialSpeed * time) + (0.5 * (acceleration * (time * time))))



