from capitals import states
import random 

print("Hi welcome to the best States game ever!!!")


# for "everything" in this array do "this" every object is a score

for score in states:
    score['correct'] = 0
    score['incorrect'] = 0
    score['counter'] = 0
    # print(score['round'])


def game_start():
    random.shuffle(states)
    round = 0
    for question in states:
        answer = input("What is the capital of " + question["name"] + "? ")
        if answer == question["capital"]:
            question['correct'] += 1
            print("yes!")
        else:
            question['incorrect'] += 1
            print("wrong!")
        print("{} right, {} incorrect".format(question['correct'],question["incorrect"]))
        question['counter'] += 1
        round += 1
        print(round)
        if round == 50:
            replay = input("Would you like to play agian? y/n ")
            if replay == "y":
                game_start()
            else: return

game_start()
# print(states)