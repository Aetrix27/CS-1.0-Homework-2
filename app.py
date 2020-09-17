# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_mood_bot_response(user_response):

    #add some bot responses to this list
    bot_response_happy = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
    bot_response_sad = ["im here for you", "sending good vibes"]
    bot_response_anxious = ["It's going to be ok"]
    bot_response_excited = ["It's great to have things to look forward to!"]
    bot_response_done = ["Goodbye, have a great day!"]

    if user_response == "happy":
        return choice(bot_response_happy)
    elif user_response == "sad":
        return choice(bot_response_sad)
    elif user_response == "anxious":
        return choice(bot_response_anxious)
    elif user_response == "excited":
        return choice(bot_response_excited)

    else:
        return "I hope your day gets better"

print("Welcome to Mood Bot")
print("Please enter how you are feeling")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while user_response != "done":
  user_response = input("How are you feeling today?: ")
  
  # Quits program when user responds with 'done'
  #if user_response == 'done':
   # break

  
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)



