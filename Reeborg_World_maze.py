def turn_right() :
    turn_left()
    turn_left()
    turn_left()
    
def north() :
    while not is_facing_north():
        turn_left()
north()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        while front_is_clear() :
            move()
            if right_is_clear() and not at_goal():
                turn_right()
                move()
    elif front_is_clear():
        while front_is_clear() and not right_is_clear():
            move()
        if right_is_clear() and not at_goal():
                turn_right()
                move()
    else :
        turn_left()