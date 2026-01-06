import os
import subprocess
import sys

cwd = os.getcwd()


def echo(message):
    print(*message)


def exit(*_):
    sys.exit()


def type(args):
    cmd = args[0]
    if cmd in builtins:
        print(f"{cmd} is a shell builtin")

    else:
        if l := find_program(cmd):
            print(f"{cmd} is {l}")
            return
        print(f"{cmd}: not found")


def pwd(_):
    print(cwd)


def cd(args):
    change_path = args[-1]
    first_char = change_path[0]
    match first_char:
        case "/":
            if os.path.exists(change_path) and os.path.isdir(change_path):
                cwd = change_path


def find_program(name):
    locations = os.environ.get("PATH", "").split(os.pathsep)
    for location in locations:
        l = os.path.join(location, name)
        if os.path.exists(l) and os.access(l, os.X_OK):
            return l
    return None


builtins = {"cd": cd, "echo": echo, "exit": exit, "pwd": pwd, "type": type}


def main():
    while True:
        user_input = input("$ ").split()

        cmd = user_input[0].lower()
        args = user_input[1:]

        if cmd in builtins:
            builtins[cmd](args)
        else:
            program = find_program(cmd)
            if program is None:
                sys.stdout.write(f"{cmd}: command not found\n")
            else:
                subprocess.run([cmd, *args])


if __name__ == "__main__":
    main()
