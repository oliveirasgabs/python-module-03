import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            num: int = int(arg)
            scores = scores + [num]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        avg: float = sum(scores) / len(scores)
        print(f"Average score: {avg}")
        high: int = max(scores)
        print(f"High score: {high}")
        low: int = min(scores)
        print(f"Low score: {low}")
        print(f"Score range: {high - low}")


if __name__ == "__main__":
    main()
