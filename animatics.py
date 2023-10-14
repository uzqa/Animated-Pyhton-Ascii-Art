import os,time
from colorama import Fore
from colorama import init as colorama_init

colorama_init(autoreset=True)

os.system("cls")
filenames = ["animated ascii/e1.txt","animated ascii/e2.txt","animated ascii/e3.txt","animated ascii/e4.txt","animated ascii/e5.txt","animated ascii/e6.txt","animated ascii/e7.txt","animated ascii/e8.txt","animated ascii/e9.txt","animated ascii/e10.txt","animated ascii/e11.txt","animated ascii/e12.txt","animated ascii/e13.txt","animated ascii/e14.txt","animated ascii/e15.txt","animated ascii/e16.txt","animated ascii/e17.txt","animated ascii/e18.txt","animated ascii/e19.txt","animated ascii/e20.txt","animated ascii/e21.txt","animated ascii/e22.txt","animated ascii/e23.txt","animated ascii/e24.txt","animated ascii/e25.txt",]
frames = []

for name in filenames:
    with open(name, "r",encoding="utf8") as f:
        frames.append(f.readlines())
for i in range(1000):
    for frame in frames:
        print(Fore.BLUE + "".join(frame) + """
                                                                  ███████  █████  ██████  ████████ ██   ██    
                                                                  ██      ██   ██ ██   ██    ██    ██   ██  
                                                                  █████   ███████ ██████     ██    ███████  
                                                                  ██      ██   ██ ██   ██    ██    ██   ██ 
                                                                  ███████ ██   ██ ██   ██    ██    ██   ██  
        """)
        time.sleep(0.4)
        os.system("cls")
