import requests
import json
import discord
from discord.ext import commands
#Settings
locationiq = ""
openweather = ""
discordtoken = ""

bot = commands.Bot(command_prefix='$', description='A weather reporting bot.')

@bot.command()
async def weather(ctx, a: str):
    lociqreq = requests.get("https://eu1.locationiq.com/v1/search.php?key=" + locationiq + "&q=" + a + "&format=json&limit=1")
    json_data = json.loads(lociqreq.text)
    lat = json_data[0]["lat"]
    lon = json_data[0]["lon"]

    openweathreq = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon +"&appid=" + openweather + "&units=metric")
    json_data1 = json.loads(openweathreq.text)
    temp = json_data1["current"]["temp"]
    conditions = json_data1["current"]["weather"][0]["description"]
    humidity = json_data1["current"]["humidity"]
    pressure = json_data1["current"]["pressure"]
    visibility = json_data1["current"]["visibility"]

    embed = discord.Embed(title=a, color=0xeee657)
    embed.add_field(name="Temperature", value="" + str(temp) + " Celcius", inline=False)
    embed.add_field(name="Current", value="" + str(conditions), inline=False)
    embed.add_field(name="Humidity", value="" + str(humidity) + "%", inline=False)
    embed.add_field(name="Pressure", value="" + str(pressure) + " hPa", inline=False)
    embed.add_field(name="Visibility", value="" + str(visibility) + " Meters", inline=False)
    embed.set_footer(text="Void#1123's WeatherBot", icon_url="https://library.kissclipart.com/20180917/csw/kissclipart-weather-icon-clipart-weather-rain-clip-art-77feae16d88a32d1.png")
    await ctx.send(embed=embed)

bot.run(discordtoken)