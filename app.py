from random import choice

#This function returns a face 3 times if the user enters that they are happy or sad.
def say_many_times(message):
    for faces in range(3):
        faces = print(message)
    return faces

#This function retrieves the mood responses from the user, and responds with an appropriate message.
def get_mood_bot_response(user_response):
    bot_response_happy = ["That's great!", "Keep smiling!", "I love to see you happy!"]
    bot_response_good = ["That's good", "Glad you're doing good!"]
    bot_response_sad = ["im here for you", "sending good vibes", "Aw, why?"]
    bot_response_anxious = ["It's going to be ok"]
    bot_response_excited = ["It's great to have things to look forward to!", "Awesome!"]
    bot_response_done = "Goodbye, have a great day!"
    bot_response_dk = ["Things will get better with time.", "I see.."]
    bot_response_joke = ["Did you hear about the mathematician that's scared of negative numbers?"
                        " He'll stop at nothing to avoid them.",
                        "Why do we tell actors to break a leg? Because every play has a cast."]

    if user_response == "happy":
        say_many_times(":)")
        return choice(bot_response_happy)
    elif user_response == "good":
        return choice(bot_response_good)
    elif user_response == "sad":
        say_many_times(":(")
        return choice(bot_response_sad)
    elif user_response == "anxious":
        say_many_times(":(")
        return choice(bot_response_anxious)
    elif user_response == "excited":
        return choice(bot_response_excited)
    elif user_response == "done":
        return bot_response_done
    elif user_response == "don't know":
        return choice(bot_response_dk)
    elif user_response == "joke":
        return choice(bot_response_joke)
    else:
        return "You can do anything you put your mind to."

print("Welcome to Chat Bot!")
print("Please enter how you are feeling, press done when you are finished talking.")

#Gets user responses until done is entered.
user_response = ""
user_responses = []
while user_response != "done":
    user_response = input("How are you feeling today?: ")
    user_responses.append(user_response)
    #Checks if user has entered a response more than once, and tells them if they have.
    #The repeat counter resets for each user response.
    repeat_counter = 0
    for response in user_responses:
        if user_response == response:
            repeat_counter+=1
        if repeat_counter>=2:
            print("You've said that more than once.. :/")

    bot_response = get_mood_bot_response(user_response)
    print(bot_response)



