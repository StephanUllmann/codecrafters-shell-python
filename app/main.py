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
    def change_to(change_path):
        global cwd
        if os.path.exists(change_path) and os.path.isdir(change_path):
            cwd = change_path.removesuffix(os.sep)
        else:
            print(f"cd: {change_path}: No such file or directory")

    change_path: str = args[-1] if len(args) > 0 else "~"
    first_char: str = change_path[0]
    match first_char:
        case os.sep:
            pass
        case "~":
            change_path = os.environ.get("HOME", "/")
        case ".":
            if "./" == change_path[:2]:
                change_path = os.path.join(cwd, change_path[2:])
            else:
                change_path = change_path.split(os.sep)
                temp_cwd = cwd.split(os.sep)
                while len(change_path) > 0 and ".." == change_path[0]:
                    temp_cwd.pop()
                    change_path.pop(0)
                change_path: str = os.path.join(
                    os.sep.join(temp_cwd), os.sep.join(change_path)
                )
        case _:
            change_path = os.path.join(cwd, change_path)

    change_to(change_path)


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
