import sys

if __name__ == "__main__":
    args = sys.argv
    length = len(args)
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if length == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
        i = 1
        while i < length:
            print(f"Argument {i}: {args[i]}")
            i += 1
    print(f"Total arguments: {length}\n")
