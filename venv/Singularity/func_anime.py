import pandas as pd
import discord

anime_data = pd.read_csv("anime_cleaned_2.csv")
anime_data.fillna("-", inplace=True)

async def anime(msg,idx = 0):

    embed = discord.Embed(title=anime_data["title"].iloc[idx],
                          description= 'Other names:\n' + anime_data['title_english'].iloc[idx] +'\n'+ anime_data['title_synonyms'].iloc[idx] +
                                      '\n' + anime_data['title_japanese'].iloc[idx] +
                                      '\n\n' + anime_data['background'].iloc[idx])

    title = anime_data['title'].iloc[idx].replace(' ','_')
    mal_link = 'https://myanimelist.net/anime/' + str(anime_data['anime_id'].iloc[idx]) + '/' + title
    embed.add_field(name="Type", value=anime_data['type'].iloc[idx])
    embed.add_field(name="Genre", value=anime_data['genre'].iloc[idx])
    embed.add_field(name="Episodes", value=anime_data['episodes'].iloc[idx])
    embed.add_field(name="Episode Length", value=anime_data['duration'].iloc[idx])
    embed.add_field(name="Status", value=anime_data['status'].iloc[idx])
    embed.add_field(name="First Aired On:", value=anime_data['premiered'].iloc[idx])
    embed.add_field(name="Score", value=anime_data['score'].iloc[idx])
    embed.add_field(name="Source", value=anime_data['source'].iloc[idx])
    embed.add_field(name="Opening", value=anime_data['opening_theme'].iloc[idx])
    embed.add_field(name="Ending", value=anime_data['ending_theme'].iloc[idx])
    embed.add_field(name="Studio", value=anime_data['studio'].iloc[idx])
    embed.add_field(name="Production", value=anime_data['producer'].iloc[idx])
    embed.add_field(name='MAL link', value=mal_link)
    await msg.channel.send(embed=embed)

#returns the most first search result
async def anime_search(msg,anime_name):
    flag = 1
    for idx in range(6668):
        if(anime_name in anime_data['title'].iloc[idx]):
            await anime(msg, idx)
            flag = 1
            break
        else:
            flag = 0

    if(flag == 0):
        await msg.channel.send("BAKA!! You made a mistake in the name!!!")


#This function returns multiple search results, instead of one
async def anime_search_2(msg,anime_name):
    flag = 0
    anime_list = []
    for idx in range(6668):
        if (anime_name in anime_data['title'].iloc[idx]):
            anime_list.append(anime_data['title'].iloc[idx])
            flag = 1
        else:
            pass
    embed = discord.Embed(title='List of Anime that match your search')
    for i in range(len(anime_list)):
        embed.add_field(name=i+1, value=anime_list[i])
    await msg.channel.send(embed=embed)

    if (flag == 0):
        await msg.channel.send("BAKA!! You made a mistake in the name!!! Remember, I'm case sensitive ;-;")