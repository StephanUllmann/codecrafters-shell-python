import sys


def main():
    while True:
        sys.stdout.write("$ ")
        cmd = ""
        for line in sys.stdin:
            cmd += line.rstrip()
            break

        sys.stdout.write(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
