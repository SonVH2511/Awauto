import time
import discord
import pyautogui
import random
from discord.ext import tasks, commands


def bait():
    pyautogui.typewrite(f"owo cf 1\n")
    # time.sleep((15))


cnt = 0
root = 25
bet = 25
money = 0
intents = discord.Intents.default()
intents.message_content = True
pyautogui.FAILSAFE = False
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID =  # tu tao kenh r dien vao day
BOT_TOKEN = "Tu set up bot r dien vao day"


@bot.event
async def on_ready():
    print(f"Bot {bot.user}  online!")
    check_messages.start()

time.sleep(2)


@tasks.loop(seconds=10)
async def check_messages():
    global bet, cnt
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print("wrong CHANNEL_ID.")
        return
    messages = [m async for m in channel.history(limit=1)]
    r = random.randint(0, 2)
    if messages:
        zf = 0
        last = messages[0]
        print(f"MSG: {last.author} → {last.content}")
        if "lost it all" in last.content:
            if (cnt >= 3):
                bait()
                bet += 1
                zf = 1
            # elif "lost it all" in last.content:
            if "spent **:cowoncy: 1**" not in last.content:
                bet *= 2
                cnt += 1
        elif "you won" in last.content:
            cnt = 0
            if "spent **:cowoncy: 1**" not in last.content:
                bet = root
        elif "Pleas​e comple​te you​r ca​ptcha t​o veri​fy" in last.content:
            time.sleep(1000000000)
        if random.randint(1, 20) > 18:
            pyautogui.typewrite("owo cash\n")
            time.sleep(5)
        if not zf:
            bet += r
            pyautogui.typewrite(f"owo cf {bet}\n")
        time.sleep(random.randint(16, 24))

bot.run(BOT_TOKEN)
