def main():
	check_beepers(clus)
	if check_beepers(clue) != 5:
		distance = 0
		while distance == 0:
			find_distance()
			advance()


def turn_around():
	turn_left()
	turn_left()
	move()	
def check_beepers(bnum):
	while on_beeper():
		bnum = 0
		pick_beeper()
		bnum += 1
	if bnum != 5:
		put_beeper
	return bnum
def find_distance():
	if front_is_clear():
		move()
		if on_beeper():

			distance = check_beeper(bnum)
			return distance

			turn_around()
			move()
		else:
			turn_around()
			move()

def get_clue():
	x= check_beepers(clue)
	if x != 5:
		return x

def get_direction():
	find_distance()
	if not front_is_clear():
		turn_left()
		find_distance()
			if not front_is_clear():
				turn_left()
				find_distance()
				if not front_is_clear():
					turn_left()
					find_distance()
	return find_distance()
def advance():
	if get_clue()== 1:
		while not facing_east():
			turn_left()
			move(distance)
	if get_clue == 2:
		while not facing_north():
			turn_left()
			move(distance)
	if get_clue == 3:
		while not facing_west():
			turn_left()
			move(distance)
	if get_clue == 2:
		while not facing_soutn():
			turn_left()
			move(distance)



