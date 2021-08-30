acceleration = 9.8
on = True

def distance_traveled(distance):
    if(distance > 100):
        print("distance traveled = ", distance, "\nGood going")
    elif(distance < 50):
        print("distance traveled = ", distance, "\nPathetic")
    else:
        print("distance traveled = ", distance, "\nnot bad")


while(on):
    initialSpeed = float(input("Enter initial speed "))

    time =float(input("Enter time of flight "))

    distance_traveled(distance = (initialSpeed * time) + (0.5 * (acceleration * (time * time))))

    decision = input("Another distance calculate? y/n ")

    if(decision == "n"):
        on = False
                    

    
