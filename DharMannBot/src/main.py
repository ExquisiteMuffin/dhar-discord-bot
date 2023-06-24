import discord
import random

bugLog = open("bugs.txt", "a")
HELP = """$dhar-quote - gives a fantastic Dhar Mann quote
$dhar-so-you-see (enter message you want) - writes a "So you see..." sentence
$dhar-bug (enter issue with bot) records any issue you have with the bot and sends it to him"""
TOKEN = 'NA'
client = discord.Client(intents=discord.Intents.all())
DHAR_QUOTES = ["'What happens in the dark always comes to light.'", 
               "'People should like you for who you are, not for what you have.'", 
               "'Your actions always have a way of coming back to you.'",
               "'Don’t let people celebrate with you at your best, if they don’t believe in you at your worst.'",
               "'In the end, love always wins.'",
               "'Whatever you believe, you can achieve.'",
               "'There are no shortcuts to success. You have to do things the right way.'"]
NO_NO_WORDS = ["Fuck", "Shit", "Ass", "Dumbass", "Nigger", "Nigga", "Bastard", "Bitch", "KYS", "retard", "ni"]
dharResponse = "HEY! We do not use such profanities. Elevate yourself to a much higher level of vocabuary than that. Remember: What happens in the dark always comes to light"
apology = "It's okay. Do better next time though, fatty."

@client.event
async def on_ready():
    #global DHAR_LOGGER
    global ACTUAL_DATE
    #DHAR_LOGGER.write(f"[{ACTUAL_DATE}]: DharMannFam has been activated \n")
    #DHAR_LOGGER.close()

@client.event
async def on_message(message):
    #global DHAR_LOGGER
    global bugLog
    global dharResponse
    global NO_NO_WORDS
    global HELP
    global ACTUAL_DATE
    user_message = str(message.content)
    user = message.author
    owner = client.get_user(573993697339899904)

    if user_message.lower() == "$help" or user_message.lower() == "$dhar":
        await message.channel.send(HELP)

    if "$dhar-bug" in user_message.lower():
        userStr = f"{user}"
        patient = user
        q = user_message.split(" ", 1)
        embed = discord.Embed(title = userStr + " reported: " + q[1])
        embed2 = discord.Embed(title = "Bug noted: " + q[1] + " -- My creator will handle this.")
        await message.channel.send(embed = embed2)
        await owner.send(embed = embed)

    #Dhar So You See...
    if "$dhar-so-you-see" in user_message.lower() and user != client.user:
        t = user_message.split(" ", 1)
        await message.channel.send(f"So you see... {t[1]}")

    #Dhar Quotes
    if "$dhar-quote" in user_message.lower() and user != client.user:
        quote = f'{DHAR_QUOTES[random.randrange(3) - 1]}'
        await message.channel.send(quote)
        #DHAR_LOGGER.write(f"[{ACTUAL_DATE}]: {user} activated DharQuote \n")
        
    #TEXT_LOGGER.write(f"[{ACTUAL_DATE}] {user} said: {user_message} \n")
    for word in range(9):
        if NO_NO_WORDS[word].lower() in user_message.lower() and user != client.user:
            await message.channel.send(dharResponse)
            break 
    
    if "sorry" in user_message.lower() and "dhar" in user_message.lower() and user != client.user:
        await message.channel.send(apology)
        
client.run(TOKEN)
