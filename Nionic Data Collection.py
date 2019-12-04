import os,time,discord
from datetime import datetime

os.system("title "+"Data Collector")

ChannelToTalkTo = 650595781081956362
AlertChannel = 650595781081956362
haveYouStartedYet = False
token = 'MzczMDkwODk1NTQ3MDcyNTEy.XeCQYw.dnoSu4mfslZgJa_R9Q57c8Y_peM'
bot = discord.Client()

print("Data Collector Bot")
print("------------------")

def runCommand(cmd):
    return os.system(cmd)

def runCommands(cmd):
    #Turn Command List To Command String
    commandList = ""
    for i in cmd:
        commandList += i + "\n"
    commandList=commandList[:-1]
    
    #Write Command String To File For Execution
    f = open("tempCommandExecution.bat",'w+')
    f.write(commandList)
    f.close()
    
    #Execute Command File
    os.system("tempCommandExecution.bat")

def logMessage(message):
    channel = message.channel
    user = message.author
    msg = message.content
    msg = msg.replace("\"","'")
    cmd = "start cmd /c python \"Log Msg.py\" \"" + str(channel) + "\" \"" + str(user) + "\" \"" + str(msg) + "\""
    runCommand(cmd)

@bot.event
async def on_ready():
    global AlertChannel
    f = open("C:/Users/Andrey/Desktop/Lookneat/My Python Scripts/Python Should It Show Message.txt",'r+')
    if (f.readline() == "T"):
        await bot.get_channel(AlertChannel).send("Data Online")
    f.close()
    
    print("Data Collector Bot Connected")

@bot.event
async def on_message(message):
    if (str(message.guild) != "Official Nionic Discord"):
        return
    
    if (str(message.content) == "Bot Status"):
        await bot.get_channel(ChannelToTalkTo).send("Bot 1 Returned: Data Bot Running")
        return
    
    logMessage(message)

bot.run(token,bot=False)
