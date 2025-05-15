# bot.py
import os
import time
import discord
from rich import print
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
import time
load_dotenv()
f = open("/Users/bigricce1227/Documents/Coding_Projects/Tokens_and_Keys/FoldBot_Token", "r")
os.environ['DISCORD_TOKEN'] = f.read()
TOKEN = os.getenv('DISCORD_TOKEN')

#print(TOKEN)
bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')
    try:
        synced = await bot.tree.sync()
        print("Commands synced up!")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(message.content)
    if message.content[:5] == '.fold':
        print("folding")
        peptide_sequence = message.content[6:]
        aminoacids = "RHKDESTNQCUGPAVILMFYW"
        foldable = True
        first_bad_char = ''
        for char in peptide_sequence:
            if aminoacids.find(char.upper()) == -1:
                foldable = False
                first_bad_char = char
        if foldable:
            await message.channel.send(f"{message.author.mention}, this sequence can be folded, please wait")
            os.environ['SEQUENCE'] = peptide_sequence.upper()
            os.environ['HAS_RETURN'] = "false"
            os.system("python inputsequence.py")
            #while('HAS_RETURN' == "false"):
            #    time.sleep(1)
            print("got return")
            await message.channel.send(f"{message.author.mention}'s protein: ")
            try:
                output = discord.File("out.zip")
                await message.channel.send(file = output)
            except FileNotFoundError:
                await message.channel.send("output was not found.")
            except Exception as e:
                await message.channel.send(f"Error: {e}")
        else:
            await message.channel.send(f"{message.author.mention}, this sequence contains invalid characters: '{first_bad_char}'")
    # some command

@bot.tree.command(name = "helpfold")
async def helpfold(interaction: discord.Interaction):
    await interaction.response.send_message(".fold: Uses the ColabFold notebook to generate pdb structures of a protein", ephemeral = True)

#@bot.tree.command(name = "alphafold2")
#@app_commands.describe(peptide_sequence = "What is the polypeptide sequence?")
#async def alphafold2(interaction: discord.Interaction, peptide_sequence: str):
#    aminoacids = "RHKDESTNQCUGPAVILMFYW"
#    foldable = True
#    first_bad_char = ''
#    for char in peptide_sequence:
#        if aminoacids.find(char.upper()) == -1:
#            foldable = False
#            first_bad_char = char
#    if foldable:
#        await interaction.response.send_message(f"{interaction.user.mention}, this sequence can be folded, please wait", ephemeral = True)
#        os.environ['SEQUENCE'] = peptide_sequence.upper()
#        os.environ['HAS_RETURN'] = "false"
#        os.system("python inputsequence.py")
#        print("got return")
#        await interaction.response.send_message(f"{interaction.user.mention}'s protein: ", ephemeral = True)
#    else:
#        await interaction.response.send_message(f"{interaction.user.mention}, this sequence contains invalid characters: '{first_bad_char}'", ephemeral = True)

bot.run(TOKEN)