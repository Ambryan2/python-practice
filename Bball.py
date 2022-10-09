import random
# making a horse game
# TODO make players
# to end the game one player has to have a length of 5
player_1 = 0
player_2 = 0
horse = 'horse'
# make these arrays filled with true and false with the amount of true being the percentage 

# make the person in terminal determine which shot Nto take then switch player 
game = input("Do you want to play horse? Y or N: ")
game = game.upper()
if game == 'Y':
    print("Let's go!!!")
    # have a value for player_1 turn count and player_2
    player_1_turns = 1
    player_2_turns = 0

    ready = input("Player one are you ready. Y or N: ")
    ready = ready.upper()
    if ready == 'Y':
        print("Good")
    else:
        print('Too bad')
    player_1_turns += 1
    while player_1 < 5 and player_2 < 5:
        # print(f"P1 = {player_1} P2 = {player_2}")
        shot_attempt = random.choice(range(0,100))
        layup = int(80 + random.choice(range(0,11)))
        mid_range = int(60 + random.choice(range(0,41)))
        three = int(35 + random.choice(range(0,41)))
        miracle = 10
        # player 1 shot option
        if player_1_turns > player_2_turns:
            shot = input("Player one what shot do you want to take (layup, mid-range, three, miracle):  ")
            shot = shot.lower()
            if shot == 'layup':
                # give players different chance shots to make  random.choice chooses randomly between a range of numbers
                if shot_attempt > layup:
                    print('missed')
                else:
                    print('Made. Player two now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > layup:
                        player_2 += 1
                        player_1_turns += 1
                        print(f"missed. Player two is now {horse[0:player_2]}")
                    else:
                        print(f"made.")
                        player_1_turns += 1
            elif shot == 'mid-range':
                if shot_attempt > mid_range:
                    print('missed')
                else:
                    print('Made. Player two now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > mid_range:
                        player_2 += 1
                        player_1_turns += 1
                        print(f"missed. Player two is now {horse[0:player_2]}")
                    else:
                        print(f"made.")
                        player_1_turns += 1
            elif shot == 'three':
                if shot_attempt > three:
                    print('missed')
                else:
                    print('Made. Player two now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > three:
                        player_2 += 1
                        player_1_turns += 1
                        print(f"missed. Player two is now {horse[0:player_2]}")
                    else:
                        print(f"made.")
                        player_1_turns += 1
            else:
                if shot_attempt > miracle:
                    print('missed')
                else:
                    print('Made. Player two now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > miracle:
                        player_2 += 1
                        player_1_turns += 1
                        print(f"missed. Player two is now {horse[0:player_2]}")
                    else:
                        print(f"made.")
                        player_1_turns += 1
            player_2_turns += 1
        # this is player 2 shot option
        else:
            shot = input("Player two what shot do you want to take (layup, mid-range, three, miracle):  ")
            shot = shot.lower()
            if shot == 'layup':
                # give players different chance shots to make  random.choice chooses randomly between a range of numbers
                if shot_attempt > layup:
                    print('missed')
                else:
                    print('Made. Player one now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > layup:
                        player_1 += 1
                        player_2_turns +=1
                        print(f"missed. Player one is now {horse[0:player_1]}")
                    else:
                        print(f"made.")
                        player_2_turns += 1
            elif shot == 'mid-range':
                if shot_attempt > mid_range:
                    print('missed')
                else:
                    print('Made. Player one now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > mid_range:
                        player_1 += 1
                        player_2_turns += 1
                        print(f"missed. Player one is now {horse[0:player_1]}")
                    else:
                        print(f"made.")
                        player_2_turns += 1
            elif shot == 'three':
                if shot_attempt > three:
                    print('missed')
                else:
                    print('Made. Player one now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > three:
                        player_1 += 1
                        player_2_turns += 1
                        print(f"missed. Player one is now {horse[0:player_1]}")
                    else:
                        print(f"made.")
                        player_2_turns += 1
            else:
                if shot_attempt > miracle:
                    print('missed')
                else:
                    print('Made. Player one now shoots the ball and ...')
                    new_shot_attempt = random.choice(range(0,100))
                    if new_shot_attempt > miracle:
                        player_1 += 1
                        player_2_turns += 1
                        print(f"missed. Player one is now {horse[0:player_1]}")
                    else:
                        print(f"made.")
                        player_2_turns += 1
            player_1_turns += 1
    if player_1 == 5:
        print('Congrats player 2!!')
    else:
        print('Congrats player 1!!')


    
elif game == 'N':
    print("Don't waste my time")
else: 
    print('Improper answer, so I no longer want to play')
