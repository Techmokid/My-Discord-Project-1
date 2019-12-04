import os,discord,win32api,re
from datetime import datetime

os.system("title "+"Swear Monitor")

print("Swear Monitor")
print("-------------")

ChannelToTalkTo = 650595781081956362
AlertChannel = 650595781081956362
haveYouStartedYet = False
token = 'MzczMDkwODk1NTQ3MDcyNTEy.XeCQYw.dnoSu4mfslZgJa_R9Q57c8Y_peM'
bot = discord.Client()

def stripCharacters(x,sub):
    if (sub):
        x = x.replace("!","i")
        x = x.replace("$","s")
        x = x.replace("#","h")
    
    return ''.join([i for i in re.sub(re.compile('\W'), '', x) if not i.isdigit()]).replace('_','').lower() 

def on_exit(sig, func=None):
    os.system("start /min cmd /c python \"Reset User Control.py\"")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Dual-control Active"))
    
    global AlertChannel
    f = open("C:/Users/Andrey/Desktop/Lookneat/My Python Scripts/Python Should It Show Message.txt",'r+')
    if (f.readline() == "T"):
        await bot.get_channel(AlertChannel).send("Swear Online")
    f.close()
    print("Swear Monitor Connected")

@bot.event
async def on_message(message):
    if (str(message.guild) != "Official Nionic Discord"):
        return
    
    if (str(message.content) == "Bot Status"):
        await bot.get_channel(ChannelToTalkTo).send("Bot 2 Returned: Swear Monitor Running")
        return
    
    with open("User Swearing Database.txt") as my_file:
        for line in my_file:
            if (stripCharacters(line,True) in stripCharacters(message.content,True)):
                await message.delete()
            if (stripCharacters(line,True) in stripCharacters(message.content,False)):
                try:
                    await message.delete()
                except:
                    pass

win32api.SetConsoleCtrlHandler(on_exit, True)
bot.run(token,bot=False)
