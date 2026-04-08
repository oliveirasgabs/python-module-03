import random
ACHIEVEMENT_LIST: list[str] = ["Crafting Genius", "Strategist", "World Savior",
                               "Speed Runner", "Survivor", "Master Explorer",
                               "Treasure Hunter", "Unstoppable", "First Steps",
                               "Collector Supreme", "Untouchable",
                               "Sharp Mind", "Boss Slayer", "Puzzle Master",
                               "Legendary Hero", "Ultimate Champion",
                               "Omaewa Mou Shindeiru"]


def gen_player_achievements() -> set[str]:
    total_achievements: int = len(ACHIEVEMENT_LIST)
    quantity: int = random.randint(0, total_achievements)
    selected_achievements: list[str] = random.sample(
        ACHIEVEMENT_LIST, quantity
    )
    return set(selected_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    all_achievements: set[str] = set(ACHIEVEMENT_LIST)

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(f"\nAll distinct achievements: {set.union(
        alice, bob, charlie, dylan)}")

    print(f"\nCommon achievements: {set.intersection(
        alice, bob, charlie, dylan)}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    print(f"\nAlice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
