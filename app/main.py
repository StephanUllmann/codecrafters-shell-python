import sys


def main():
    while True:
        cmd = input("$ ")
        sys.stdout.write(f"{cmd}: command not found\n")


if __name__ == "__main__":
    main()
