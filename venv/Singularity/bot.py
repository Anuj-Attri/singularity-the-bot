import discord
import random
from func_poke import pokemon
from function1 import quote, helpbox
from func_anime import anime,anime_search,anime_search_2

prefix = '$'
TOKEN = ' '
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'pat'):                                        
        msg = '>///< {0.author.mention}'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith(prefix + 'quote'):
       await message.channel.send(quote() + "\n{0.author.mention}".format(message))

    elif message.content == (prefix + 'help'):
        await helpbox(message)
        await message.channel.send("**:heart_decoration: Help has been sent to you~ :heart_decoration:**")

    elif message.content.startswith(prefix + 'anime'):
        await anime(message, random.randint(1, 6668))

    elif message.content.startswith(prefix + 'asearch'):
        content = message.content.replace(prefix + 'asearch ','')
        await anime_search(message, content)

    elif message.content.startswith(prefix + 'list '):
        content = message.content.replace(prefix + 'list ','')
        await anime_search_2(message,content)

    elif message.content.startswith(prefix + 'dex '):
        content = message.content.replace(prefix + 'dex ','')
        await pokemon(message, content)

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with @Ałvārez~"))

client.run(TOKEN)
