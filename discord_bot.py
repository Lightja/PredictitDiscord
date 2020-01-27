import main
import auths
import discord
import requests
import json

api = main.Api()
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    elif message.content.startswith("'Hello") or message.content.startswith("'hello") or \
         message.content.startswith(",Hello") or message.content.startswith(",hello"):
        print(message.channel)
        await message.channel.send('Hello')
    elif message.content.startswith("'murder") or message.content.startswith("'kill") or \
         message.content.startswith(",murder") or message.content.startswith(",kill"):
        msg = "oh no you have killed me\n"
        msg += "I am ded"
        await message.channel.send(msg)
    elif message.content.startswith("'Risk") or message.content.startswith("'risk") or message.content.startswith("'r ") or \
         message.content.startswith(",Risk") or message.content.startswith(",risk") or message.content.startswith(",r "):
        argument = message.content.split(' ')
        if len(argument) > 2:
            try:
                shares = int(argument[-1])
                market = argument[1:-1]
                minimum = True
            except:
                market = argument[1:]
                shares = 850
                minimum = False
        else:
            shares = 850
            minimum = False
            market = argument[1:]
        whole = ""
        for part in market:
            whole += part + " "
        market = whole[:-1]
        print("Risk")
        print(market, shares, message.author)
        if market == 'top' or market == 'all':
            risk = api.optimize_all(max_shares=shares)
            await message.channel.send(risk)
        else:
            title, info, url = api.get_market_risk(market, shares, minimum)
            embed = discord.Embed(title=title, url=url,
                                  description=info)
            await message.channel.send(embed=embed)
    elif message.content.startswith("'Bins") or message.content.startswith("'bins") or message.content.startswith("'b ") or \
         message.content.startswith(",Bins") or message.content.startswith(",bins") or message.content.startswith(",b "):
        argument = message.content.split(' ')
        market = argument[1:]
        whole = ""
        for part in market:
            whole += part + " "
        market = whole.strip()
        title, bins, url = api.get_market_bins(market)
        embed = discord.Embed(title=title, url=url,
                              description=bins)
        print("Bins")
        print(market, message.author)
        await message.channel.send(embed=embed)
    elif message.content.startswith("'Help") or message.content.startswith("'help") or message.content.startswith("'h ") or \
         message.content.startswith(",Help") or message.content.startswith(",help") or message.content.startswith(",h "):
        msg = ""
        msg += "Hello, I am a helpful PredictIt bot\n"
        msg += "I can perform various helpful tasks. Just say a command then either the market id or part of the market's name\n"
        msg += "Here are the commands I can perform:\n"
        msg += "  ,help or ,h brings up this message.\n"
        msg += "  ,risk or ,r can be used to figure out whether a market has negative risk or not. The keyword 'all' searches all the markets.\n"
        msg += "  ,bins or ,b can be used to show the prices for each bin in a market.\n"
        msg += "  ,value or ,v can be used to compare the cost of buying Yes and buying no on everything else.\n"
        msg += "  ,market or ,m can be used to get all the markets that contain the input in the title.\n"
        msg += "  ,- can be used to get all the markets that contain the input in the title.\n"
        msg += "  ,. can be used to get all the markets that contain the input in the one of the bins.\n"
        msg += "  ,o can be used to get the volume of the contracts in a specific market.\n"
        msg += "  ,rcp can be used get the current rcp averages for the nation or individual states.\n"
        msg += "This bot took a while to make, and as a broke college student, I'd really appreciate a donation if you make any money off predictit...\n"
        msg += "   Bitcoin: bc1qxmm7l2vhema687hrvle3yyp04h6svzy8tkk8sg\n"
        msg += "   PayPay, Venmo, etc: PM @crazycrabman#2555\n"
        msg += "The bot is running on AWS, so it should be online 24/7. If it isn't, you have an idea for another command, or just want to chat about this bot, PM @crazycrabman#2555\n"
        print("Help")
        print(message.author)
        await message.channel.send(msg)
    elif message.content.startswith("'v ") or message.content.startswith("'value") or message.content.startswith("'Value") or \
         message.content.startswith(",v ") or message.content.startswith(",value") or message.content.startswith(",Value"):
        argument = message.content.split(' ')
        if len(argument) > 2:
            try:
                bin = int(argument[-1])
                market = argument[1:-1]
            except:
                market = argument[1:]
                bin = 0
        else:
            bin = 0
            market = argument[1:]
        whole = ""
        for part in market:
            whole += part + " "
        market = whole.strip()
        msg = api.value_buy(market, bin - 1)
        print("Value")
        print(market, bin, message.author)
        await message.channel.send(msg)
    elif message.content.startswith("'m ") or message.content.startswith("'market") or message.content.startswith("'Market") or \
         message.content.startswith(",m ") or message.content.startswith(",market") or message.content.startswith(",Market"):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        if 'bin' in keyword:
            keyword = keyword.strip('bin').strip()
            msg = api.get_related_market_bins(keyword)
        else:
            msg = api.get_related_markets(keyword)
        print("bins")
        print(keyword, message.author)
        await message.channel.send(msg)
    elif message.content.startswith("'. ") or message.content.startswith(",. "):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        msg = api.get_related_market_bins(keyword)
        print("Similar")
        print(keyword, message.author)
        await message.channel.send(msg)
    elif message.content.startswith("'- ") or message.content.startswith(",- "):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        msg = api.get_related_markets(keyword)
        print("Similar")
        print(keyword, message.author)
        await message.channel.send(msg)
    elif message.content.startswith("'o ") or message.content.startswith(",o "):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        title, msg, url = api.discord_orderbook(keyword)
        embed = discord.Embed(title=title, url=url,
                              description=msg)
        print("Offers")
        print(keyword, message.author)
        await message.channel.send(embed=embed)
    elif message.content.startswith("'rcp") or message.content.startswith(",rcp"):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        if keyword.lower() == 'iowa' or keyword.lower() == 'ia':
            msg = "Getting RCP average for Iowa\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6731_historical.js").text[12:][:-2]
        elif keyword.lower() == 'nv' or keyword.lower() == 'nevada':
            msg = "Getting RCP average for Nevada\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6866_historical.js").text[12:][:-2]
        elif keyword.lower() == 'nh' or keyword.lower() == 'new hampshire':
            msg = "Getting RCP average for New Hampshire\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6276_historical.js").text[12:][:-2]
        elif keyword.lower() == 'sc' or keyword.lower() == 'south carolina':
            msg = "Getting RCP average for South Carolina\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6824_historical.js").text[12:][:-2]
        elif keyword.lower() == 'national' or keyword.lower() == 'nation':
            msg = "Getting RCP average for the nation\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6730_historical.js").text[12:][:-2]
        elif keyword.lower() == 'california' or keyword.lower() == 'ca':
            msg = "Getting RCP average for California\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6879_historical.js").text[12:][:-2]
        elif keyword.lower() == 'texas' or keyword.lower() == 'tx':
            msg = "Getting RCP average for Texas\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6875_historical.js").text[12:][:-2]
        elif keyword.lower() == 'massachusetts' or keyword.lower() == 'ma':
            msg = "Getting RCP average for Massachusetts\n```\n"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6786_historical.js").text[12:][:-2]
        averages = json.loads(averages)
        max_len = 0
        for candidate in averages['poll']['rcp_avg'][0]['candidate']:
            if len(candidate['name']) > max_len and candidate['value']:
                max_len = len(candidate['name'])
        msg += "Name" + '  ' + (' ' * (max_len - 4)) + "Average\n"
        for candidate in averages['poll']['rcp_avg'][0]['candidate']:
            if candidate['value']:
                msg += candidate['name'] + '  ' + (' ' * (max_len - len(candidate['name']))) + str(
                    candidate['value']) + '\n'
        msg += '```'
        print("RCP")
        print(keyword, message.author)
        await message.channel.send(msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(auths.discord_token)
