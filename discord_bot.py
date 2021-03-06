import asyncio
import main
import auths
import discord
import requests
import json
import yfinance as yf
from model import Model

api = main.Api()
client = discord.Client()
stats = {'users': {}, 'commands': {}}
nevada_first = Model("nevada", "02-22", 1)
nevada_second = Model("nevada", "02-22", 2)
nevada_third = Model("nevada", "02-22", 3)


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
    elif message.content.startswith(",vote") or message.content.startswith(",hack") or message.content.startswith(
            ",rig"):
        await message.channel.send("Can't do that unfortunately, I'm not Russian")
    elif message.content.startswith("!burn") or message.content.startswith(",burn"):
        await message.channel.send("No U")
    elif message.content.startswith(",tip") or message.content.startswith(",donate"):
        msg = "This bot took a while to make, and as a broke college student, I'd really appreciate a donation if you make any money off predictit...\n"
        msg += "    Bitcoin: \n    bc1qxmm7l2vhema687hrvle3yyp04h6svzy8tkk8sg\n"
        msg += "    PayPay, Venmo, etc: \n    PM @crazycrabman#2555\n"
        await message.channel.send(msg)
    elif message.content.startswith(",Risk") or message.content.startswith(",risk") or message.content.startswith(
            ",r "):
        stats['commands']['risk'] = stats['commands'].get('risk', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        stats['commands']['bins'] = stats['commands'].get('bins', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        stats['commands']['rcp'] = stats['commands'].get('rcp', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        stats['commands']['search_bins'] = stats['commands'].get('search_bins', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        stats['commands']['search_titles'] = stats['commands'].get('search_titles', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,donate)")
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
        stats['commands']['orderbook'] = stats['commands'].get('orderbook', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
    elif message.content.startswith(",rcp") or message.content.startswith(",RCP"):
        stats['commands']['rcp'] = stats['commands'].get('rcp', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
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
    elif message.content.startswith(",stock") or message.content.startswith(",s "):
        stats['commands']['stocks'] = stats['commands'].get('stocks', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        stats['commands']['help'] = stats['commands'].get('help', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
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
        msg += ",i or ,implied gets the implied odds of each candidate winning the presidency (% pres / % nom). \n"
        msg += "\n"
        msg += "This bot took a while to make, and as a broke college student, I'd really appreciate a donation if like the bot or find it useful.\n"
        msg += "    Bitcoin: \n    bc1qxmm7l2vhema687hrvle3yyp04h6svzy8tkk8sg\n"
        msg += "    PayPay, Venmo, etc: \n    PM @crazycrabman#2555\n"
        msg += "The bot is running on AWS, so it should be online 24/7. If it isn't, you have an idea for another command, or just want to chat about this bot, PM @crazycrabman#2555\n"
        print("Help")
        print(message.author)
        embed = discord.Embed(title=title, description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",i") or message.content.startswith(",implied"):
        stats['commands']['implied'] = stats['commands'].get('implied', 0) + 1
        stats['users'][message.author] = stats['users'].get(message.author, 0) + 1
        if stats['users'][message.author] % 100 == 0:
            await message.channel.send("I see you've been using the bot quite a bit. Please consider donating some of your winnings! (,tip)")
        msg = api.divide_bins(3698, 3633)
        embed = discord.Embed(title="Implied dem presidential victory odds", description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",stats"):
        msg = ""
        for user, num in stats['users'].items():
            msg += user.name + ": " + str(num) + '\n'
        embed = discord.Embed(title="user stats", description=msg, color=2206669)
        await message.channel.send(embed=embed)
        msg = ""
        for command, num in stats['commands'].items():
            msg += command + ": " + str(num) + '\n'
        embed = discord.Embed(title="command stats", description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",nv2"):
        print("Getting Nevada Second Results")
        split = message.content.split(' ')
        argument = split[1:]
        whole = ""
        for part in argument:
            whole += part + " "
        argument = whole.strip()
        if not argument:
            results = nevada_second.merged_totals()
        else:
            results = nevada_second.best_county(argument)
        msg = '```\n'
        for key, value in sorted(results.items(), key=lambda x:- x[1]):
            msg += key + " " * (11 - len(key)) + str(value) + " " * (7 - len(str(value))) + str(round(value/(results['Total'])*100, 2)) + "%\n"
        msg += '```\n'
        embed = discord.Embed(title="NV Second Alignment", description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",nv3"):
        print("Getting Nevada Final Results")
        split = message.content.split(' ')
        argument = split[1:]
        whole = ""
        for part in argument:
            whole += part + " "
        argument = whole.strip()
        if not argument:
            results = nevada_third.merged_totals()
        else:
            results = nevada_third.best_county(argument)
        msg = '```\n'
        for key, value in sorted(results.items(), key=lambda x:- x[1]):
            msg += key + " " * (11 - len(key)) + str(value) + " " * (7 - len(str(value))) + str(round(value/(results['Total'])*100, 2)) + "%\n"
        msg += '```\n'
        embed = discord.Embed(title="NV Final Delegates", description=msg, color=2206669)
        await message.channel.send(embed=embed)
    elif message.content.startswith(",nv") or message.content.startswith(",nv1"):
        print("Getting Nevada First Results")
        split = message.content.split(' ')
        argument = split[1:]
        whole = ""
        for part in argument:
            whole += part + " "
        argument = whole.strip()
        if not argument:
            results = nevada_first.merged_totals()
        else:
            results = nevada_first.best_county(argument)
        msg = '```\n'
        for key, value in sorted(results.items(), key=lambda x: -x[1]):
            msg += key + " " * (11 - len(key)) + str(value) + " " * (7 - len(str(value))) + str(round(value/(results['Total'])*100, 2)) + "%\n"
        msg += '```\n'
        embed = discord.Embed(title="NV First Alignment", description=msg, color=2206669)
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
    old1 = {'Klobuchar': 1, 'Sanders': 0, 'Warren': 0, 'Yang': 0, 'Steyer': 0, 'Biden': 0, 'Buttigieg': 0, 'Bloomberg': 0, 'Total': 0}
    old2 = {'Klobuchar': 1, 'Sanders': 0, 'Warren': 0, 'Yang': 0, 'Steyer': 0, 'Biden': 0, 'Buttigieg': 0, 'Bloomberg': 0, 'Total': 0}
    old3 = {'Klobuchar': 1, 'Sanders': 0, 'Warren': 0, 'Yang': 0, 'Steyer': 0, 'Biden': 0, 'Buttigieg': 0,
            'Bloomberg': 0, 'Total': 0}
    while client.is_ready():
        print("checking results")
        changed = False
        results1 = nevada_first.merged_totals()
        results2 = nevada_second.merged_totals()
        results3 = nevada_third.ap.get_totals()
        if results1 != old1:
            old1 = results1
            print("new results1")
            msg = '```\n'
            for key, value in sorted(results1.items(), key=lambda x: -x[1]):
                msg += key + " " * (11 - len(key)) + str(value) + " " * (7 - len(str(value))) + str(
                    round(value / (results1['Total'] + 1) * 100, 2)) + "%\n"
            msg += '```\n'
            embed = discord.Embed(title="NV First Alignment", description=msg, color=2206669)
            await client.get_channel(671281289105768449).send(embed=embed)
        if results2 != old2:
            old2 = results2
            print("new results2")
            msg = '```\n'
            for key, value in sorted(results2.items(), key=lambda x: -x[1]):
                msg += key + " " * (11 - len(key)) + str(value) + " " * (7 - len(str(value))) + str(
                    round(value / (results2['Total'] + 1) * 100, 2)) + "%\n"
            msg += '```\n'
            embed = discord.Embed(title="NV Second Alignment", description=msg, color=2206669)
            await client.get_channel(680708890245202015).send(embed=embed)
        if results3 != old3:
            old3 = results3
            print("new results2")
            msg = '```\n'
            for key, value in sorted(results3.items(), key=lambda x: -x[1]):
                if key != "precinct_counted" and key != "precinct_total":
                    msg += key + " " * (11 - len(key)) + str(value) + " " * (7 - len(str(value))) + str(
                        round(value / (results3['Total'] + 1) * 100, 2)) + "%\n"
            msg += '```\n'
            embed = discord.Embed(title="NV Final Delegates", description=msg, color=2206669)
            await client.get_channel(680708890245202015).send(embed=embed)
        await asyncio.sleep(5)


client.loop.create_task(my_background_task())
client.loop.create_task(poll_check())
client.run(auths.discord_token)
