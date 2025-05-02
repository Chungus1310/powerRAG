import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from rag_system import search_and_generate_response

# Hey! This loads our secret stuff from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Setting up what our bot can do
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Let's everyone know we're up and running!
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.command(name='ask')
async def ask(ctx, *, question):
    # Time to be helpful and answer some questions!
    loading_message = await ctx.send("Processing your question, please wait...")
    
    try:
        answer = search_and_generate_response(question)
        
        embed = discord.Embed(
            title="Business Information",
            description=answer,
            color=discord.Color.blue()
        )
        embed.set_footer(text="Powered by Gemini 2.0")
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error: {str(e)}")
    finally:
        await loading_message.delete()

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)