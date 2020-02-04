import asyncio
import main
import auths
import discord
import requests
import json
import yfinance as yf

api = main.Api()
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    elif message.content.startswith(",Hello") or message.content.startswith(",hello"):
        await message.channel.send('Hello')
    elif message.content.startswith(",Bye") or message.content.startswith(",bye"):
        await message.channel.send('Bye')
    elif message.content.startswith(",murder") or message.content.startswith(",kill"):
        msg = "oh no you have killed me\n"
        msg += "I am ded"
        await message.channel.send(msg)
    elif message.content.startswith(",vote") or message.content.startswith(",hack") or message.content.startswith(",rig"):
        await message.channel.send("Can't do that unfortunately, I'm not Russian")
    elif message.content.startswith("!burn") or message.content.startswith(",burn"):
        await message.channel.send("No U")
    elif message.content.startswith(",tip") or message.content.startswith(",donate"):
        msg = "This bot took a while to make, and as a broke college student, I'd really appreciate a donation if you make any money off predictit...\n"
        msg += "    Bitcoin: \n    bc1qxmm7l2vhema687hrvle3yyp04h6svzy8tkk8sg\n"
        msg += "    PayPay, Venmo, etc: \n    PM @crazycrabman#2555\n"
        await message.channel.send(msg)
    elif message.content.startswith(",Risk") or message.content.startswith(",risk") or message.content.startswith(",r "):
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
            title, info = api.optimize_all(max_shares=shares)
            embed = discord.Embed(title=title, description=info, color=2206669)
            await message.channel.send(embed=embed)
        else:
            title, info, url = api.get_market_risk(market, shares, minimum)
            embed = discord.Embed(title=title, url=url,
                                  description=info, color=2206669)
            await message.channel.send(embed=embed)
    elif message.content.startswith(",Bins") or message.content.startswith(",bins") or message.content.startswith(
            ",b "):
        argument = message.content.split(' ')
        market = argument[1:]
        whole = ""
        for part in market:
            whole += part + " "
        market = whole.strip()
        title, bins, url = api.get_market_bins(market)
        embed = discord.Embed(title=title, url=url,
                              description=bins, color=2206669)
        print("Bins")
        print(market, message.author)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",v ") or message.content.startswith(",value") or message.content.startswith(
            ",Value"):
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
    elif message.content.startswith(",. "):
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
    elif message.content.startswith(",- "):
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
    elif message.content.startswith(",o "):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        title, msg, url = api.discord_orderbook(keyword)
        embed = discord.Embed(title=title, url=url,
                              description=msg, color=2206669)
        print("Offers")
        print(keyword, message.author)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",rcp") or message.content.startswith(",RCP") or message.content.startswith(",p"):
        argument = message.content.split(' ')
        keyword = argument[1:]
        whole = ""
        for part in keyword:
            whole += part + " "
        keyword = whole.strip()
        if keyword.lower() == 'iowa' or keyword.lower() == 'ia':
            title = "RCP average for Iowa"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6731_historical.js").text[12:][:-2]
        elif keyword.lower() == 'nv' or keyword.lower() == 'nevada':
            title = "RCP average for Nevada"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6866_historical.js").text[12:][:-2]
        elif keyword.lower() == 'nh' or keyword.lower() == 'new hampshire':
            title = "RCP average for New Hampshire"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6276_historical.js").text[12:][:-2]
        elif keyword.lower() == 'sc' or keyword.lower() == 'south carolina':
            title = "RCP average for South Carolina"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6824_historical.js").text[12:][:-2]
        elif keyword.lower() == 'national' or keyword.lower() == 'nation':
            title = "RCP average for the nation"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6730_historical.js").text[12:][:-2]
        elif keyword.lower() == 'california' or keyword.lower() == 'ca':
            title = "RCP average for California"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6879_historical.js").text[12:][:-2]
        elif keyword.lower() == 'texas' or keyword.lower() == 'tx':
            title = "RCP average for Texas"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6875_historical.js").text[12:][:-2]
        elif keyword.lower() == 'massachusetts' or keyword.lower() == 'ma':
            title = "RCP average for Massachusetts"
            averages = requests.get("https://www.realclearpolitics.com/epolls/json/6786_historical.js").text[12:][:-2]
        averages = json.loads(averages)
        max_len = 0
        for candidate in averages['poll']['rcp_avg'][0]['candidate']:
            if len(candidate['name']) > max_len and candidate['value']:
                max_len = len(candidate['name'])
        msg = "```Name" + '  ' + (' ' * (max_len - 4)) + "Average\n"
        for candidate in averages['poll']['rcp_avg'][0]['candidate']:
            if candidate['value']:
                msg += candidate['name'] + '  ' + (' ' * (max_len - len(candidate['name']))) + str(
                    candidate['value']) + '\n'
        msg += '```'
        print("RCP")
        print(keyword, message.author)
        embed = discord.Embed(title=title, description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",alert") or message.content.startswith(",a"):
        argument = message.content.split(' ')
        keywords = argument[1:]
        value = int(keywords.pop(-1))
        bin = int(keywords.pop(-1)) - 1
        market = int(keywords.pop(-1))
        if len(keywords) > 0:
            await message.channel.send('Expected 3 arguments')
        print(message.author)
        user = '<@' + str(message.author.id) + '>'
        api.log_alert(user, market, bin, value)
        msg = "Setting alert for market " + str(market) + "\n"
        if value > 0:
            msg += "This alert will trigger when B" + str(bin + 1) + " goes above " + str(value) + '¢'
        else:
            msg += "This alert will trigger when B" + str(bin + 1) + " goes below " + str(-value) + '¢'
        await message.channel.send(msg)
    elif message.content.startswith(",stock") or message.content.startswith(",s"):
        argument = message.content.split(' ')
        market = argument[1:]
        whole = ""
        for part in market:
            whole += part + " "
        market = whole.strip()
        data = yf.Ticker(market)
        try:
            await message.channel.send(market + " is currently trading at $" + str(data.info['regularMarketPrice']))
        except IndexError:
            await message.channel.send(market + " not found")
    elif message.content.startswith(",Help") or message.content.startswith(",help") or message.content.startswith(",h"):
        title = "Here are the commands I can perform:\n"
        msg = ",help or ,h brings up this message.\n"
        msg += ",risk or ,r figures out whether a market has negative risk or not. The keyword 'all' searches all the markets.\n"
        msg += ",bins or ,b shows the prices for each bin in a market.\n"
        msg += ",value or ,v compares the cost of buying Yes and buying no on everything else.\n"
        msg += ",- gets all the markets that contain the input in the title.\n"
        msg += ",. gets all the markets that contain the input in the one of the bins.\n"
        msg += ",o gets the volume of the contracts in a specific market.\n"
        msg += ",rcp or ,p gets the current rcp averages for the nation or individual states.\n"
        msg += ",stock or ,s gets the last traded price of the indicated ticker. \n"
        msg += "\n"
        msg += "This bot took a while to make, and as a broke college student, I'd really appreciate a donation if you make any money off predictit...\n"
        msg += "    Bitcoin: \n    bc1qxmm7l2vhema687hrvle3yyp04h6svzy8tkk8sg\n"
        msg += "    PayPay, Venmo, etc: \n    PM @crazycrabman#2555\n"
        msg += "The bot is running on AWS, so it should be online 24/7. If it isn't, you have an idea for another command, or just want to chat about this bot, PM @crazycrabman#2555\n"
        print("Help")
        print(message.author)
        embed = discord.Embed(title=title, description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",dmr") or message.content.startswith(",d"):
        print(message)
        results = requests.get(
            "https://features.desmoinesregister.com/news/politics/iowa-caucuses-results-alignment/newresults.json").json()
        race_0 = results['races'][3]['reportingUnits'][0]['candidates']
        title = "DMR Iowa Results"
        msg = ""
        for result in race_0:
            try:
                msg += result['last'] + " - " + str(result['voteCount']) + '\n'
            except KeyError:
                pass
        print("DRM Update")
        embed = discord.Embed(title=title, description=msg, color=2206669,
                              url="https://features.desmoinesregister.com/news/politics/iowa-caucuses-results-alignment/")
        await message.channel.send(embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def my_background_task():
    await client.wait_until_ready()
    print('starting')
    while client.is_ready():
        messages = api.get_messages()
        for i, message in enumerate(messages):
            if message:
                await client.get_channel(671281289105768449).send(message)
                messages[i] = None
        api.messages = [message for message in messages if message is not None]
        await asyncio.sleep(30)


async def poll_check():
    await client.wait_until_ready()
    old = {"Bernie": 1804, "Elizabeth": 1633, "Pete": 1553, "Amy": 771, "Joe": 722}
    while client.is_ready():
        results = requests.get("https://features.desmoinesregister.com/news/politics/iowa-caucuses-results-alignment/newresults.json").json()
        race_0 = results['races'][3]['reportingUnits'][0]['candidates']
        changed = False
        for result in race_0:
            try:
                num = old[result['first']]
                if num != result['voteCount']:
                    changed = True
                old[result['first']] = result['voteCount']
            except KeyError:
                pass
        if changed:
            title = "DMR Results Changed"
            msg = ""
            for result in race_0:
                try:
                    msg += result['last'] + " - " + str(result['voteCount']) + '\n'
                except KeyError:
                    pass
            print("DRM Update")
            embed = discord.Embed(title=title, description=msg, color=2206669, url="https://features.desmoinesregister.com/news/politics/iowa-caucuses-results-alignment/")
            await client.get_channel(670891620996218900).send(embed=embed)
        await asyncio.sleep(5)

client.loop.create_task(my_background_task())
client.loop.create_task(poll_check())
client.run(auths.discord_token)
