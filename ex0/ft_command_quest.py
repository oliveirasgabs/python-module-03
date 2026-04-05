import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    len_args: int = len(sys.argv)
    if len_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len_args - 1}")
        i: int = 0
        while i < len_args - 1:
            print(f"Argument {i + 1}: {sys.argv[i + 1]}")
            i += 1
    print(f"Total arguments: {len_args}")


if __name__ == "__main__":
    main()
