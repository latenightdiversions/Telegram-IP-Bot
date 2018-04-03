from telepot.loop import MessageLoop
import telepot
import time
import ipgetter

#reads everything in from chat
def handle(msg):

    #gets basic information about the incoming message
    content_type, chat_type, chat_id = telepot.glance(msg)

    # must be text, private chat, and by specified user
    if (content_type == 'text') and (chat_type == 'private') and ((msg['from']['username'] == initUsername)):

        # super sexy library by @phoemur on github
        ip = ipgetter.myip()

        # sends message to user
        bot.sendMessage(chat_id, ip)

    # ensures this will not function in a group chat
    elif (chat_type != 'private'):
        bot.sendMessage(chat_id, "IP address can only be displayed in a private chat.")

    # assumes somebody else who is not authorized is communicatig with the bot
    else:
        bot.sendMessage(chat_id, "You are not authorized to view this IP address.")

#sets initial user info, will not run without correct information
# if somebody else gets your bot name, they won't get your IP if the username is incorrect
initUsername = input("Telegram Username: ")
token = input("Bot Token: ")

# starts bot
bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()

# if this shows up it probably is going to work
print ("Listening ... my dude.")

# Keep the program running.
while 1:
    time.sleep(10)
