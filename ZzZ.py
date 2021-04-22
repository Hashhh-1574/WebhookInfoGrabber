#libraries
import msvcrt
import os
try:
    from dhooks import Webhook
except:
    os.system("py -m pip install dhooks")
    from dhooks import Webhook
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
    
init()
os.system("title 𝗗𝗜𝗦𝗖𝗢𝗥𝗗 𝗪𝗘𝗕𝗛𝗢𝗢𝗞 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡")
banner = (Fore.MAGENTA + """▒███████▒▒███████▒▒███████▒
▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░
░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ 
  ▄▀▒   ░  ▄▀▒   ░  ▄▀▒   ░     Coded: Hashhh#1574
▒███████▒▒███████▒▒███████▒
░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒
░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒
░ ░ ░ ░ ░░ ░ ░ ░ ░░ ░ ░ ░ ░
  ░ ░      ░ ░      ░ ░    
░        ░        ░       Webhook Information Grabber""")

print(banner)
hook = Webhook(input(" WEBHOOK : "))
hook.get_info()
print(f"\n GUILD ID    : {hook.guild_id}")
print(f" CHANNEL ID  : {hook.channel_id}")
print(f" USERNAME    : {hook.default_name}")
print(f" IMAGE       : {hook.default_avatar_url}")

msvcrt.getch()
