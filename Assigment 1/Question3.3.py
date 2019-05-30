import re

def createChatBox(usertext):
    replytext = re.sub(r".*name is (\w+)", r"Hi \1.", usertext, flags=re.IGNORECASE)
    replytext = re.sub(r".*Can you (\w+)", r"Yes I can definitely \1", replytext, flags=re.IGNORECASE)
    replytext = re.sub(r"\?", r".", replytext, flags=re.IGNORECASE)
    replytext = re.sub(r".*you are (\w+)", r"Thank you. You are just as \1 as I am", replytext, flags=re.IGNORECASE)
    replytext = re.sub(r".*name?", r"My name is Cooper", replytext, flags=re.IGNORECASE)
    replytext = re.sub(r" me.| me ", r" you ", replytext, flags=re.IGNORECASE)

    print(replytext)


usertext = input("Hello, how may I help you? \n(When you are done chatting to me please type \"Bye\")\n")

while usertext != "Bye":
    createChatBox(usertext)
    usertext = input()

print("GoodBye :)")
