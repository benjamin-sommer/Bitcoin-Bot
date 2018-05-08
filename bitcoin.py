import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import requests
import json

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot is ready and connected to Discord")

@client.event
async def on_message(message):
    if message.content.lower() == "btc":
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        responseJSON = json.loads(response.text)

        price = ("£" + responseJSON["bpi"]["GBP"]["rate"])

        userID = message.author.id
        await client.send_message(message.channel, (("<@%s> The price of a Bitcoin is " + price) % (userID)))

    if message.content.lower() == "btc loop":
        userID = message.author.id
        for i in range(1, 15):

            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            responseJSON = json.loads(response.text)

            price = ("£" + responseJSON["bpi"]["GBP"]["rate"])

            await client.send_message(message.channel, (("<@%s> The price of a Bitcoin is " + price) % (userID)))

            time.sleep(60)


client.run("<TOKEN>")
