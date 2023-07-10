import discord, datetime, random
from jungEdigganervmichnichtduscheisskek import token_e
from settings import startdate, prefix, last_date, server
from discord.utils import get

async def send_message(message, user_nachricht, author = None):
    try:
        if "user" in user_nachricht:
            userE = discord.Embed(title = author, color = discord.Color(0xef67bb),description="test")
            userE.set_author(name =author.name, icon_url=author.avatar)

            await message.channel.send(embed=userE)
        else:
            antwort = react(user_nachricht,message)
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

franzosen = [398907038798970891,568390435177758741, 419198918023184385, 500720535315939328]

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
        guild = message.guild

        print(f"{username} said: '{user_message}' ({channel})")


        if message.guild == client.get_guild(server):
            author = message.author
            for i in range(4, len(user_message)):
                if user_message[i] == "-":
                    if user_message[i+1] =="<":
                        author = client.get_user(int(user_message[i+3:-1]))
                    else:
                        author = client.get_user(int(user_message[i+1:]))
                    print(author, user_message[i+3:-2])

            if user_message[0] == prefix:
                user_message = user_message[1:].strip()  # [1:] Removes the '?'
                await send_message(message, user_message, author)
            

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

        if "franzosenjail" in user_message and message.channel == client.get_channel(807273390385266711):
            if ".t" in user_message:
                for user in franzosen:
                    franzose = message.guild.get_member(user)
                    await franzose.remove_roles(get(franzose.guild.roles, name="zugriff"))
                    await franzose.add_roles(get(franzose.guild.roles, name="franzoser"))
                try:
                    await message.channel.send("franzosenjail set to true")
                except Exception as e:
                    print(e)
            if ".f" in user_message:
                for user in franzosen:
                    franzose = message.guild.get_member(user)
                    await franzose.add_roles(get(franzose.guild.roles, name="zugriff"))
                    await franzose.remove_roles(get(franzose.guild.roles, name="franzoser"))
                try:
                    await message.channel.send("franzosenjail set to false")
                except Exception as e:
                    print(e)
            
    client.run(TOKEN)


def react(nachricht_e, message):
    global prefix
    nachricht = nachricht_e.lower()
    print("ee")
    # if nachricht == "user":
    #     async def e():
    #         try:
    #             userE = discord.Embed(title = str(message.author), color = discord.Color(000000),description="test")
    #             await message.channel.send(embed =userE) 
    #         except Exception as e:
    #             print(e)
    #     return 0

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
