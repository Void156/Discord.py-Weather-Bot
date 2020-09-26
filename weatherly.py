from weatherly import bot
import json
with open('settings.json', 'r') as settingsfile:
    settings = json.loads(settingsfile.read())
bot.run(settings['discordtoken'])