import re

def createChatBox(usertext):
    print(usertext)


usertext = input("Hello, how may I help you?")

while usertext != "-1":
    createChatBox(usertext)
    usertext = input()

print("GoodBye :)")
