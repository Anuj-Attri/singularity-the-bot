import pandas as pd
import random
import discord

data = pd.read_csv("quotes.csv")
data["Author"].fillna("Anonymous", inplace=True)

def quote():
    idx = random.randint(1,1664)
    return ('```' + data["Quote"].iloc[idx] + '\n-' + data["Author"].iloc[idx] + '```')

async def helpbox(msg):
    help_em = discord.Embed(title="Help is Here~", description="Heyaa!!! Lemme help you, UwU~ \nThe Prefix is:$ ")
    help_em.add_field(name='help', value='Shows help (pfft you already did that, baka!!)')
    help_em.add_field(name='pat', value='ME LIKEY PATS!!!')
    help_em.add_field(name='quote', value='Shows a famous quote~\n MOTIVATION!!!')
    help_em.add_field(name='anime', value='Shows a random anime (yayyyy!!)')
    help_em.add_field(name='asearch',
                      value='I\'ll try my best to search for the anime you want UwU \nI\'m case sensitive ;-; , please be gentle~')
    help_em.add_field(name='list', value='Gives back multiple anime from search~')
    help_em.add_field(name='dex', value='Searches for a pokemon and it\'s stats!!')
    await msg.author.send(embed=help_em)

##await message.channel.send('M-matte kudasai!!')