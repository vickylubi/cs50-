from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()

    #count input argumetns 
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet.getFonts():
                font = sys.argv[2]
            else: 
                sys.exit()
        else: 
            sys.exit()
    else:
        sys.exit("Too many arguments")
        
    figlet.setFont(font=font)
    
    s = input("What do you want to write")
    print(figlet.renderText(s))
    
if __name__ == "__main__":
    main()