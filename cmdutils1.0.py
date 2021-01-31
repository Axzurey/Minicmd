import requests
import socket
import os
import winsound
import tkinter as tk
import random
import time
import sys
import pyperclip
from pythonping import ping
import webbrowser
from time import strftime 

user = os.getlogin()
P1 = ""

def qlread():
    try:
        with open(".\\textfolder\\Quicklaunch.txt", "r") as v:
            urls = v.readline()
            global Q1
            global Q2
            global Q3
            global Q4
            global Q5
            Q1, Q2, Q3, Q4, Q5 = urls.split(",", 5)
            v.close()
    except (ValueError, NameError, TypeError):
        cmdoutput.configure(text=" Unable to read Quicklaunch folder")


def copybutton():
    p2 = cmdoutput.cget("text")
    pyperclip.copy(p2)


def command_start():
    global P1
    P1 = cmdpanel.get().lower().strip()
    try:
        param1, param2, param3, waste1 = P1.split(" ", 4)
        del waste1
        del param3
        if param1 == "ping":
            cmd_ip_ping()
        elif param1 == "random":
            cmd_random_int()  
        elif param1 == "qb" and param2 == "change":
            cmd_quicklaunch_change()
        else:
            cmdoutput.configure(text="Unknown command or invalid parameters. \n do 'help get list' to get a list of commands")
    except (NameError, TypeError, ValueError):
        try:
            param1, param2, param3 = P1.split(" ", 3)
            if param1 == "ip" and param2 == "get":
                cmd_ip_get()
            elif param1 == "ip" and param2 == "status":
                cmd_ip_status()
            else:
                cmdoutput.configure(text="Unknown command or invalid parameters. \n do 'help get list' to get a list of commands")
        except (NameError, TypeError, ValueError):
            try:
                param1, param2 = P1.split(" ", 2)
                if param1 == "coinflip":
                    cmd_coinflip()
                elif param1 == "encoding":
                    cmd_encoding_get()
                elif param1 == "rps":
                    cmd_rps()
                elif param1 == "open":
                    cmd_url_open()
                else: 
                    cmdoutput.configure(text="Unknown command or invalid parameters. \n do 'help get list' to get a list of commands")
            except (NameError, TypeError, ValueError):
                try:
                    param1 = P1
                    if param1 == "help":
                        cmd_help()
                    elif param1 == "draw":
                        cmd_draw()
                    else:
                        cmdoutput.configure(text="Unknown command or invalid parameters. \n do 'help get list' to get a list of commands")
                except (NameError, TypeError, ValueError):
                    cmdoutput.configure(text="Unknown command or invalid parameters. \n do 'help get list' to get a list of commands")

def cmd_quicklaunch_change():
    try:
        param1, param2, param3, param4 = P1.split(" ", 4)
        Qv = int(param4)
        Qv = Qv - 1
        del param1
        del param2
        with open(".\\textfolder\\Quicklaunch.txt", "r") as Tx:
            try:
                urls = Tx.readline()
                T1, T2, T3, T4, T5 = urls.split(",", 5)
                try:
                    with open(".\\textfolder\\Quicklaunch.txt", "w") as Tx2:
                        if Qv == 0:
                            T1 = param3
                            Tx2.write(T1 + "," + T2 + "," + T3 + "," + T4 + "," + T5)
                            cmdoutput.configure(text=param3 + "has been added to Quick Launch \n Clicking the button will take you to the changed website but the text will not update until an application restart")
                            Tx2.close()
                            qlread()
                        elif Qv == 1:
                            T2 = param3
                            Tx2.write(T1 + "," + T2 + "," + T3 + "," + T4 + "," + T5)
                            cmdoutput.configure(text=param3 + "has been added to Quick Launch \n Clicking the button will take you to the changed website but the text will not update until an application restart")
                            Tx2.close()
                            qlread()
                        elif Qv == 2:
                            T3 = param3
                            Tx2.write(T1 + "," + T2 + "," + T3 + "," + T4 + "," + T5)
                            cmdoutput.configure(text=param3 + "has been added to Quick Launch \n Clicking the button will take you to the changed website but the text will not update until an application restart")
                            Tx2.close()
                            qlread()
                        elif Qv == 3:
                            T4 = param3
                            Tx2.write(T1 + "," + T2 + "," + T3 + "," + T4 + "," + T5)
                            cmdoutput.configure(text=param3 + "has been added to Quick Launch \n Clicking the button will take you to the changed website but the text will not update until an application restart")
                            Tx2.close()
                            qlread()
                        elif Qv == 4:
                            T5 = param3
                            Tx2.write(T1 + "," + T2 + "," + T3 + "," + T4 + "," + T5)
                            cmdoutput.configure(text=param3 + "has been added to Quick Launch \n Clicking the button will take you to the changed website but the text will not update until an application restart")
                            Tx2.close()
                            qlread()
                        else:
                            Tx2.write(T1 + "," + T2 + "," + T3 + "," + T4 + "," + T5)
                            cmdoutput.configure(text="Something went wrong trying to add that to Quick Launch")
                            Tx2.close()
                            qlread()
                except (NameError, ValueError, TypeError):
                    cmdoutput.configure(text="Invalid or missing parameter(s)")
            except (NameError, ValueError, TypeError):
                cmdoutput.configure(text="Invalid or missing parameter(s)")
    except (NameError, ValueError, TypeError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")
    

def cmd_url_open():
    try:
        param1, param2 = P1.split(" ", 2)
        del param1
        webbrowser.open(param2, 1)
        cmdoutput.configure(text=" Opening url... \n if it did not open in your default browser try prefixing it with 'http://' or 'https://'")
    except (NameError, ValueError, TypeError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")


def cmd_help():
    try:
        webbrowser.open(".\\textfolder\\help.txt")
        cmdoutput.configure(text="opened help notepad as a new window")
    except (FileNotFoundError):
        cmdoutput.configure(text="Help file not found...")


def cmd_draw():
    global P1
    P1 = cmdpanel.get().lower().strip()
    try:
        param1 = P1
        del param1
        playernum = random.randint(0, 9)
        botnum = random.randint(0, 9)
        if botnum < playernum:
            botnum = str(botnum)
            playernum = str(playernum)
            cmdoutput.configure(text=" The bot got a: " + botnum + " and you got a: " + playernum + ". you won!")
        elif botnum > playernum:
            botnum = str(botnum)
            playernum = str(playernum)
            cmdoutput.configure(text=" The bot got a: " + botnum + " and you got a: " + playernum + ". you lost!")
        elif botnum == playernum:
            botnum = str(botnum)
            playernum = str(playernum)
            cmdoutput.configure(text=" The bot got a: " + botnum + " and you got a: " + playernum + ". you both tied!")
    except (NameError, TypeError, ValueError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")


def cmd_ip_ping():
    global P1   
    P1 = cmdpanel.get().lower().strip()
    try:
        param1, param2, param3, param4 = P1.split(" ", 4)
        del param1
        param3 = int(param3)
        param4 = int(param4)
        try:
            pigned_list = ping(param2, size=param3, count=param4)
            avgms = str(pigned_list.rtt_avg_ms)
            lowms = str(pigned_list.rtt_min_ms)
            highms = str(pigned_list.rtt_max_ms)
            param2 = str(param2)
            param3 = str(param3)
            param4 = str(param4)
            cmdoutput.configure(text=" Ping to : " + param2 + " \n Packet size: " + param3 + " \n Packet count: " + param4 + " \n Rtt average ms: " + avgms + "\n Lowest ms: " + lowms + " \n Highest ms: " + highms)
        except (requests.exceptions.RequestException, socket.gaierror):
            cmdoutput.configure(text="Unable to ping url")
        except (ValueError, NameError):
            cmdoutput.configure(text="Invalid syntax")
    except (NameError, TypeError, ValueError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")

def cmd_ip_get():
    global P1   
    P1 = cmdpanel.get().lower()
    try:
        param1, param2, param3 = P1.split(" ", 3)
        del param1 
        del param2
        try:
            pulled_ip = socket.gethostbyname(param3)
            cmdoutput.configure(text=pulled_ip)
        except (requests.exceptions.RequestException, socket.gaierror):
            cmdoutput.configure(text="Unable to locate Url")
        except (ValueError, NameError):
            cmdoutput.configure(text="Invalid or missing parameter(s)")
    except (NameError, TypeError, ValueError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")
        


def cmd_ip_status():
    global P1   
    P1 = cmdpanel.get().lower()
    try:
        param1, param2, param3 = P1.split(" ", 3)
        del param1
        del param2
        try:
            response = os.system("ping " + param3 + " -n 1")
            if response == 0:
                cmdoutput.configure(text=param3 + " is up")
            else:
                cmdoutput.configure(text=param3 + " is down")
        except (requests.exceptions.RequestException, socket.gaierror, OSError):
            cmdoutput.configure(text="Unable to locate url")
        except (ValueError, NameError, TypeError):
            cmdoutput.configure(text="Unexpected error occured")
    except (NameError, TypeError, ValueError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")


def cmd_random_int():
    global P1   
    P1 = cmdpanel.get().lower()
    try:
        param1, param2, param3, param4 = P1.split(" ", 4)
        del param1
        try:
            param2n = int(param2)
            param3n = int(param3)
            param4n = int(param4)
            randnum = random.sample(range(param2n, param3n), param4n)
            randstring = str(randnum)   
            cmdoutput.configure(text=randstring)
        except (ArithmeticError):
            cmdoutput.configure(text="Arithmetic error occured")
        except (ValueError, NameError, TypeError):
            cmdoutput.configure(text="Invalid or missing parameter(s)")
    except (ValueError, NameError, TypeError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")


def cmd_encoding_get():
    global P1   
    P1 = cmdpanel.get().lower()
    try:
        param1, param2 = P1.split(" ", 2)
        del param1
        try:
            loads = {'things': 2, 'total': 25}
            r = requests.get(param2, params=loads)
            cmdoutput.configure(text=r.encoding)
        except requests.exceptions.RequestException:
                cmdoutput.configure(text="Unable to locate url... Did you forget the 'https' prefix?")
        except (ValueError, NameError, TypeError):
                cmdoutput.configure(text="Invalid or missing parameter(s)")
    except (ValueError, NameError, TypeError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")


def cmd_coinflip():
    tailscount = 0
    headscount = 0
    global P1   
    P1 = cmdpanel.get().lower()
    try:
        param1, param2 = P1.split(" ", 2)
        del param1
        param2 = int(param2)
        rolls = 0
        try:
            while rolls < param2:
                randchoice = random.randint(1, 2)
                if randchoice == 1:
                    tailscount += 1
                    rolls += 1
                else:
                    headscount += 1
                    rolls += 1
            else:
                tailscountA = str(tailscount)
                headscountA = str(headscount)
                cmdoutput.configure(text="Tails was flipped " + tailscountA + " times!" " Heads was flipped " + headscountA + " times!")
        except (ValueError, NameError, TypeError, ArithmeticError):
            cmdoutput.configure(text="Error occured")
    except (ValueError, NameError, TypeError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")


def cmd_rps():
    global P1   
    P1 = cmdpanel.get().lower().strip()
    try:
        param1, param2 = P1.split(" ", 2)
        del param1
        botpick1 = random.randint(1, 3)
        playerpick = param2
        botpick = ""
        if botpick1 == 1:
            botpick = "rock"
        elif botpick1 == 2:
            botpick = "paper"
        elif botpick1 == 3:
            botpick = "scissors"
        
        if playerpick == "rock" and botpick == "paper":
            cmdoutput.configure(text=" You lost! The bot picked: " + botpick)
        elif playerpick == "paper" and botpick == "rock":
            cmdoutput.configure(text=" You win! The bot picked: " + botpick)
        elif playerpick == "scissors" and botpick == "rock":
            cmdoutput.configure(text=" You lost! The bot picked: " + botpick)
        elif playerpick == "rock" and botpick == "scissors":
            cmdoutput.configure(text=" You win! The bot picked: " + botpick)
        elif playerpick == "paper" and botpick == "scissors":
            cmdoutput.configure(text=" You lost! The bot picked: " + botpick)
        elif playerpick == "scissors" and botpick == "paper":
            cmdoutput.configure(text=" You win! The bot picked: " + botpick)
        elif playerpick == botpick:
            cmdoutput.configure(text=" Draw! both picked: " + playerpick)
        else:
            cmdoutput.configure(text="Invalid choice... please pick either 'rock, paper, or scissors'.")
    except (ValueError, NameError, TypeError):
        cmdoutput.configure(text="Invalid or missing parameter(s)")

qlread()
def QuickLch1():
    webbrowser.open(Q1, 1)


def QuickLch2():
    webbrowser.open(Q2, 1)


def QuickLch3():
    webbrowser.open(Q3, 1)


def QuickLch4():
    webbrowser.open(Q4, 1)


def QuickLch5():
    webbrowser.open(Q5, 1)

window = tk.Tk()
window.title("Cmdutils")
window.geometry("800x600")
photo = tk.PhotoImage(file= r".\\images\\cmdutil.png")
window.iconphoto(False, photo)
mainbg = tk.PhotoImage(file= r".\\images\\background.png")
mainbg = mainbg.zoom(3, 3)

# frames and pseudo frames
mainframe = tk.Label(window, bg="#00ffff", image=mainbg)
mainframe.place(relwidth=1, relheight=0.9, rely=0.1)

picframe = tk.Label(window, bg="#c800ff")
picframe.place(relwidth=1, relheight=0.1, rely=0)

# widgets
cmdpanel = tk.Entry(mainframe, text="Input command", font="arial, 35", fg="black", bg="white")
cmdpanel.place(relx=0.1, rely=0.1, relwidth=0.50, relheight=0.1)

cmdoutput = tk.Label(mainframe, text="Output", anchor="nw", wraplength=700, justify="left", bg="white")
cmdoutput.place(relx=0.01, rely=0.25, relwidth=0.70, relheight=0.5)

outputcopy = tk.Button(mainframe, height=3, width=15, text="Copy output", cursor="cross", highlightcolor="blue", bg="#eaff00", command=copybutton)
outputcopy.place(relx=0.22, rely=0.88, relwidth=0.2, relheight=0.1)

Run = tk.Button(mainframe, height=3, width=15, text="Run command", cursor="cross", highlightcolor="blue", bg="#eaff00", command=command_start)
Run.place(relx=0.01, rely=0.88, relwidth=0.2, relheight=0.1)

ql1 = tk.Button(mainframe, height=3, width=15, text="Open in browser: \n " + Q1, cursor="cross", highlightcolor="blue", bg="#ff6f00", command=QuickLch1)
ql1.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)

ql2 = tk.Button(mainframe, height=3, width=15, text="Open in browser: \n " + Q2, cursor="cross", highlightcolor="blue", bg="#ff6f00", command=QuickLch2)
ql2.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.1)

ql3 = tk.Button(mainframe, height=3, width=15, text="Open in browser: \n " + Q3, cursor="cross", highlightcolor="blue", bg="#ff6f00", command=QuickLch3)
ql3.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.1)

ql4 = tk.Button(mainframe, height=3, width=15, text="Open in browser: \n " + Q4, cursor="cross", highlightcolor="blue", bg="#ff6f00", command=QuickLch4)
ql4.place(relx=0.75, rely=0.5, relwidth=0.2, relheight=0.1)

ql5 = tk.Button(mainframe, height=3, width=15, text="Open in browser: \n " + Q5, cursor="cross", highlightcolor="blue", bg="#ff6f00", command=QuickLch5)
ql5.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.1)

def clocktime(): 
    string = strftime('%H:%M:%S %p') 
    clock.config(text = string) 
    clock.after(1000, clocktime) 
  

clock = tk.Label(window, font = ('calibri', 20), bg = 'black', fg = 'white') 
  
clock.place(relx=0.9, rely=0.95, relwidth=0.1, relheight=0.05)
clocktime()

window.mainloop()
# for future reference. The script never got to this part because of the above mainloop(). Michael you were too imcompetent to realize the fact that mainloop is a LOOP and is INFINITE
# this means the things below will never run. Ever.
try:
    pic2 = open(".\\images\\cmdutil.png", "r")
    pic3 = open(".\\images\\background.png", "r")
    helptxt = open(".\\textfolder\\help.txt", "r")
    qltxt = open(".\\textfolder\\Quicklaunch.txt", "r")
    pic2.close()
    helptxt.close()
    qltxt.close()
    pic3.close()
except (FileNotFoundError):
    cmdoutput.configure(text=" 1 or more files not found")
