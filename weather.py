import aiohttp
import json
import discord
from discord.ext import commands


#Import Settings - Dont edit here, edit the settings.json file.
with open('settings.json', 'r') as myfile:
    settingsfile = myfile.read()
    settings = json.loads(settingsfile)
locationiq = settings["locationiq"]
openweather = settings["openweather"]
discordtoken = settings["discordtoken"]
prefix = settings["prefix"]

bot = commands.Bot(command_prefix='' + prefix, description='A weather reporting bot.')
@bot.event
async def on_ready():
    print("Warning you are using the dev version!!!!")
    print("Bot Ready.")
@bot.command()
async def weather(ctx, a: str):
    async with aiohttp.ClientSession() as session:
        async with  session.get("https://eu1.locationiq.com/v1/search.php?key=" + locationiq + "&q=" + a + "&format=json&limit=1") as resploc:
            data = await resploc.text()
            json_data = json.loads(data)
            try:
                lat = json_data[0]["lat"]
                lon = json_data[0]["lon"]
                async with session.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon +"&appid=" + openweather + "&units=metric") as respope:
                    data1 = await respope.text()
                    json_data1 = json.loads(data1)
                    temp = json_data1["current"]["temp"]
                    conditions = json_data1["current"]["weather"][0]["description"]
                    humidity = json_data1["current"]["humidity"]
                    pressure = json_data1["current"]["pressure"]
                    visibility = json_data1["current"]["visibility"]

                embed = discord.Embed(title=a, color=0x57eee6)
                embed.add_field(name="Temperature", value="" + str(temp) + " Celcius", inline=False)
                embed.add_field(name="Current", value="" + str(conditions), inline=False)
                embed.add_field(name="Humidity", value="" + str(humidity) + "%", inline=False)
                embed.add_field(name="Pressure", value="" + str(pressure) + " hPa", inline=False)
                embed.add_field(name="Visibility", value="" + str(visibility) + " Meters", inline=False)
                embed.set_footer(text="Weatherly Stable", icon_url="https://library.kissclipart.com/20180917/csw/kissclipart-weather-icon-clipart-weather-rain-clip-art-77feae16d88a32d1.png")
                await ctx.send(embed=embed)
            except KeyError:
                await ctx.send("Error, invalid city.")
       

bot.run(discordtoken)