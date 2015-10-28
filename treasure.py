#OLA 108 by kres wright, CSCI 1170-009
#PROGRAM ID: treasure.py/ Following the Treasure Map Task
#Remarks: This program allows Reeborg to follow clues to the 'treasure'
#(distance corner with 5 beepers)

#main function
def main():
    direction = beepers_on_corner()
    while direction != 5:
        distance = distance_clue()
        face_direction(distance)
        move_foward(distance)
        direction = beepers_on_corner()
    celebrate()
    turn_off()

#returns number of beepers on corner
def beepers_on_corner():
    count = 0
    while on_beeper():
        pick_beeper()
        count += 1
    for i in range(count):
        put_beeper()
    return count

#get distance clue
def distance_clue():
    distance = 0    
    while distance == 0:
        if front_is_clear():
            move()
            if on_beeper():
                distance = beepers_on_corner()
                while carrying_beepers():
                    put_beeper()
                turn_around()
            else:
                turn_around()
                if front_is_clear():
                    turn_left()
                else:
                    if not left_is_clear():
                        turn_right()
        else:
            turn_left()
    return distance

#turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#turn around 180 degrees and move to original spot
def turn_around():
    turn_left()
    turn_left()
    move()
#face direction clue gives

def face_direction(direction):
    direction = beepers_on_corner()
    if direction == 1:
        while not facing_east():
            turn_left()
    elif direction == 2:
        while not facing_north():
            turn_left()
    elif direction == 3:
        while not facing_west():
            turn_left()
    else:
        direction == 4
        while not facing_south():
            turn_left()
#move number of corners in clue
def move_foward(distance):
    for i in range(distance):
        move()
#celebrate finding treasure
def celebrate():
    while on_beeper():
        pick_beeper()
    while not facing_north():
        turn_left()
main()




    
    
            
