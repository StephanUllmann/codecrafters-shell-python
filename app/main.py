import os
import sys


def echo(message):
    print(*message)


def exit(*_):
    sys.exit()


def type(args):
    cmd = args[0]
    if cmd in builtins:
        print(f"{cmd} is a shell builtin")

    else:
        locations = os.environ.get("PATH", "").split(os.pathsep)
        for location in locations:
            l = os.path.join(location, cmd)
            if os.path.exists(l):
                print(f"{cmd} is {l}")
                return
        print(f"{cmd}: not found")


builtins = {"echo": echo, "exit": exit, "type": type}


def main():
    while True:
        user_input = input("$ ").split()

        cmd = user_input[0].lower()
        args = user_input[1:]

        if cmd not in builtins:
            sys.stdout.write(f"{cmd}: command not found\n")
        else:
            builtins[cmd](args)


if __name__ == "__main__":
    main()
