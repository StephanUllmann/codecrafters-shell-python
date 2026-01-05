import sys


def main():
    while True:
        cmd = input("$ ")
        if "exit" == cmd.lower():
            break
        sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
