# main.py

from command_handler import CommandHandler
def printCoolStyledMouse():
    # ANSI escape codes for colors
    red = "\033[38;2;255;0;0m"      # Bright Red for *
    orange = "\033[38;2;255;165;0m" # Orange
    yellow = "\033[38;2;255;255;0m" # Yellow
    green = "\033[38;2;0;255;0m"    # Green
    cyan = "\033[38;2;0;255;255m"   # Cyan
    blue = "\033[38;2;0;0;255m"     # Blue
    purple = "\033[38;2;127;0;255m" # Purple
    reset = "\033[0m"               # Reset to default

    # Create the ASCII art line by line with colors
    art = [
        "                                           .-+*******=-:         .--:.                                                 ",
        "                                      :********:               +%###**#%#*                                             ",
        "                                  :***+:=**.                   *#+**     .*%-                                          ",
        "                                =**+.:**                        #*.******+- :**%%%#+                                  ",
        "                              +**= :*-                 .::::.    +#:.+*******+*****##%%*                               ",
        "                            -**+ :*-          :+#%%%###########%###%#*==****************#%*                            ",
        "                           +**= **         *#%%#**************************************#***###                          ",
        "                          ***- **       :#%##*******************************************#***##*                        ",
        "                         +**= *+       #%#******************+=::::-+**************************##-                      ",
        "                        :*** +#      .#%#**********#####*.           =*************************#%+                     ",
        "                        +**: #+      %%#***************####%*       .****##%##**##%##**********###:                    ",
        "                        *** :#:     *%#********+            *#%     :**###-          :+*##%%#*=.                       ",
        "                        *** -#=     *##*******        *+.      =     =*##                                              ",
        "                        *#*.:#*     *%#******:         -##             *##%*                                           ",
        "                        =#*= ##:    =%#******.         .#%####%%%##*-     =###                                         ",
        "                         ##* :##     #%#**+-:.:-+*##%%%%%#*+-:::=*###%%#-   .#%=                                       ",
        "                         +##* +%#     *%#********+:                 :**#%#-   *%=                                      ",
        "                          *%#+ =%#:     *%###*****##%%#%%%%%%#%#*     :**%%=   .#                                      ",
        "                           +%#*.:#%*       :=***++=-::.        :*%#:   =*##%     :                                     ",
        "                            :#%*= =%%#.                          -%#   :*#%%.                                          ",
        "                              *##*-.*##%#:                       *##   +*#%#                                           ",
        "                                *##*+=**##%%#*:                =###   =**##:                                           ",
        "                                  -#%##******##%%%%#########%%%#*.  :**#%#.                                            ",
        "                                     :#####*******************:  -***#%#-                                              ",
        "                                         :*#%%###***************##%%#*                                                 ",
        "                                               :=**##%%%%#%%%%#*+:                                                     ",
        "                                                                                                                       ",
        "                                                                     by  pingplus/pingminus                             "
    ]

    # Loop through each line and print with alternating colors
    for line in art:
        colored_line = ''
        for char in line:
            if char == '*':
                # Cycling colors for *
                colored_line += red  # Change this to any color you like
            else:
                # Greyish background for all other characters
                colored_line += "\033[38;2;100;100;100m"  # Dark grey for other characters
            colored_line += char  # Add the character to the line
        print(colored_line + reset)  # Reset color at the end of each line


if __name__ == '__main__':
    print("\033[38;2;0;0;255mAll-In-One Terminal v.0.1.4\033[0m")
    printCoolStyledMouse()
    print(f"\033[92mEnter 'help' to see available commands':")
    command_handler = CommandHandler()
    command_handler.wait_for_input()
