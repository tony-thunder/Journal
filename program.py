import journaler
import file_manager


def header():
    print("""
    ===================================
                JOURNAL
    ===================================
          """)


def command_loop():
    cmd = None

    while cmd != 'x':
        print("Welcome to the Journal program.")
        cmd = input('Command (m for menu):')
        cmd = cmd.lower().strip()

        if cmd == 'm':
            menu()
        elif cmd == 'a':
            disabled(cmd)
        elif cmd == 'c':
            disabled(cmd)
        elif cmd == 'e':
            disabled(cmd)
        elif cmd == 'l':
            disabled(cmd)
        elif cmd == 'n':
            disabled(cmd)
        elif cmd == 'o':
            disabled(cmd)
        elif cmd == 'q':
            disabled(cmd)
        elif cmd == 's':
            disabled(cmd)
        elif cmd != 'x':
            print("Invalid Command")


def menu():
    print("""
           a   add tag to entry
           c   close journal"
           e   add entry to open journal
           l   list entries in journal
           m   print this menu
           n   new journal file
           o   open journal
           q   query tags
           s   save journal
           x   exit journal program""")


def disabled(cmd):
    print("{} is not a valid command at this time.".format(cmd))

def main():
    header()
    command_loop()


main()