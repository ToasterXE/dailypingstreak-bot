import discord, datetime, random
from jungEdigganervmichnichtduscheisskek import token_e
from settings import startdate, prefix, last_date

async def send_message(message, user_nachricht):
    try:    
        antwort = react(user_nachricht)
        await message.channel.send(antwort)
    except Exception as e:
        print(e)

daten = []
prefix_index = 1
start_index = 2
last_index = 3
e = [last_date, startdate]

intents = discord.Intents.all()
with open("settings.py") as datei:
    for line in datei:
        daten.append(line.strip())
    datei.close()



def run_discord_bot():
    global last_date, e, startdate
    TOKEN = token_e
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):

        if message.author == client.user:
            return
        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == prefix:
            user_message = user_message[1:].strip()  # [1:] Removes the '?'
            await send_message(message, user_message)
        
        elif "<@&869885593977520128>" in user_message:
            last_date = e[0]
            if (datetime.date.today() - last_date).days <= 1:
                last_date = datetime.date.today()
                e[0] = last_date
                daten[last_index] = f"last_date = datetime.date({last_date.year},{last_date.month},{last_date.day})"
                with open("settings.py",mode="w") as datei:
                    for i in range(0,len(daten)):
                        datei.write(daten[i] + "\n")
                    datei.close
            
            else:
                startdate = datetime.date.today()
                e[1] = startdate
                last_date = datetime.date.today()
                e[0] = last_date
                daten[last_index] = f"last_date = datetime.date({last_date.year},{last_date.month},{last_date.day})"
                daten[start_index] = f"startdate = datetime.date({startdate.year},{startdate.month},{startdate.day-1})"
                with open("settings.py",mode="w") as datei:
                    for i in range(0,len(daten)):
                        datei.write(daten[i] + "\n")
                    datei.close 

        elif "<:komischesetwas:949028421781028864>" in user_message:
            if random.randint(1,5) == 1:
                await send_message(message, user_message)


    client.run(TOKEN)


def react(nachricht_e):
    global prefix
    nachricht = nachricht_e.lower()

    if nachricht == "<:komischesetwas:949028421781028864>":
            return "<:komischesetwas:949028421781028864>"

    if "prefix" in nachricht:
        prefix = nachricht[-1]
        daten[prefix_index] = f"prefix = \"{prefix}\""
        with open("settings.py",mode="w") as datei:
            for i in range(0,len(daten)):
                datei.write(daten[i] + "\n")
        datei.close
        return str("Prefix set to " + prefix)


    if nachricht == "test":
        return "e"

    if nachricht == "streak":
        return str("Die letzte Unterbrechung des Streaks war am " + str(e[1]) + ", seit dem sind " + str((e[0] - e[1]).days) + " Tage vergangen.")

run_discord_bot()
