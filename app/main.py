import sys


def echo(message):
    print(*message)


def main():
    while True:
        user_input = input("$ ").split()

        cmd = user_input[0].lower()
        args = user_input[1:]

        match cmd:
            case "exit":
                break
            case "echo":
                echo(args)
            case _:
                sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
