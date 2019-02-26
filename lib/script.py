from capitals import states
import random 

print("Hi welcome to the best States game ever!!!")

def game_start():
    round = 0
    random.shuffle(states)


# for "everything" in this array do "this" every object is a score

for score in states:
    score['correct'] = 0
    score['incorrect'] = 0
    score['counter'] = 0
    # print(score['round'])


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


print(states)