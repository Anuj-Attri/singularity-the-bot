import discord
import pandas as pd
import random

poke_data = pd.read_csv('Pokemon_2.csv')
poke_data.fillna('None', inplace=True)
colors = [0x0000FF, 0xFF0000, 0x00FF00, 0x000000, 0xFFFFFF]


async def poke_embed(msg, idx):
    path = "C:/Users/Anuj Attri/PycharmProjects/singularity-the-bot/venv/Singularity/images/" + str(
        poke_data['Name'].iloc[idx]).lower() + '.png'
    file = discord.File(path,filename=str(poke_data['Name'].iloc[idx]).lower() + '.png')
    embed = discord.Embed(title=str(poke_data['Name'].iloc[idx]).upper(), color=colors[random.randint(0,6)])
    embed.add_field(name='Primary Type', value=poke_data['Type 1'].iloc[idx])
    embed.add_field(name='Secondary Type', value=poke_data['Type 2'].iloc[idx])
    embed.add_field(name='Total', value=poke_data['Total'].iloc[idx])
    embed.add_field(name='Attack', value=poke_data['Attack'].iloc[idx])
    embed.add_field(name='Defense', value=poke_data['Defense'].iloc[idx])
    embed.add_field(name='Special Attack', value=poke_data['Sp. Atk'].iloc[idx])
    embed.add_field(name='Special Defense', value=poke_data['Sp. Def'].iloc[idx])
    embed.add_field(name='Speed', value=poke_data['Speed'].iloc[idx])
    embed.set_thumbnail(url='attachment://' + str(poke_data['Name'].iloc[idx]).lower() + '.png')

    await msg.channel.send(file=file,embed=embed)


async def pokemon(msg, poke_name):
    flag = 0
    for idx in range(800):
        if poke_name == str(poke_data['Name'].iloc[idx]).lower():
            flag = 1
            await poke_embed(msg, idx)
            break
        elif poke_name == poke_data['Name'].iloc[idx]:
            flag = 1
            await poke_embed(msg, idx)
            break

    if flag == 0:
        await msg.channel.send('Not found!!!')


