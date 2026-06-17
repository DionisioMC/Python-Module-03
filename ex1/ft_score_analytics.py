import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args: list[int] = []
    for arg in sys.argv[1:]:
        try:
            args.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(args) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("Scores processed: [", end="")
        i = 0
        while i < len(args) - 1:
            print(f"{args[i]}, ", end="")
            i += 1
        print(f"{args[i]}]")
        print(f"Total players: {len(args)}")
        print(f"Total score: {sum(args)}")
        print(f"Average score: {sum(args) / len(args)}")
        print(f"High score: {max(args)}")
        print(f"Low score: {min(args)}")
        print(f"Score range: {max(args) - min(args)}\n")
