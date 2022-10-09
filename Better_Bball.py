
import random
player_1 = 0
player_2 = 0

horse = 'horse'
player_1_turns = 1
player_2_turns = 0

people = [[player_1, player_1_turns, 'Player 1'],[player_2, player_2_turns, 'Player 2']]

while people[0][0] < 5 and people[1][0] < 5:

    shot_attempt = random.choice(range(0,101))

    options = {'layup':int(80 + random.choice(range(0,11))),'mid':int(60 + random.choice(range(0,41))),'three':int(35 + random.choice(range(0,66))),'miracle':10}
    # this determines which player is selected
    if people[0][1] > people[1][1]:
        turn = 0
        other = 1
    else: 
        turn = 1
        other = 0

    # this is the input for shot 
    shot = input(f"{people[turn][2]} what shot do you want to take (layup, mid, three, miracle):  ")
    shot = shot.lower()

    # if shot is an incorrect
    if shot != 'layup' and shot != 'mid' and shot != 'three' and shot != 'miracle':
        print("\tMissed because you didn't type correctly")

    # this is the for loop that looks for shot in input and then determines if shot is made for one person
    for choice in list(options.keys()):
        if shot == choice:
            if shot_attempt > options[choice]:
                print('\tMissed')
            else:
                options = {'layup':int(80 + random.choice(range(0,11))),'mid':int(40 + random.choice(range(0,41))),'three':int(25 + random.choice(range(0,26))),'miracle':10}
                print(f"\tYou made it {people[turn][2]}!")
                new_shot_attempt = random.choice(range(0,101))
                if new_shot_attempt > options[choice]:
                    people[other][0] += 1 #this adds to opposing player score 
                    people[turn][1] += 1 #this adds one to current player turn so that they shoot again 
                    print(f"\t{people[other][2]} missed. {people[other][2]} is now {horse[0:people[other][0]]}")
                else:    
                    print(f"\t {people[other][2]} made it!")
                    people[turn][1] += 1
    people[other][1] += 1 #this adds one to the player who didn't start the shot

if player_1 == 5:
    print('\tCongrats player 1')
else: 
    print('\tCongrats player 2')
