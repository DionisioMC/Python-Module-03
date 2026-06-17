import random


def gen_player_achievements() -> None:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    alice = set(random.sample(achievements, k=6))
    print(f"Player Alice: '{alice}")
    bob = set(random.sample(achievements, k=7))
    print(f"Player Bob: '{bob}")
    charlie = set(random.sample(achievements, k=9))
    print(f"Player Charlie: '{charlie}")
    dylan = set(random.sample(achievements, k=5))
    print(f"Player Dylan: '{dylan}\n")
    achievements_set = set(achievements)
    print(f"All distinct achievements: {achievements_set}\n")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")
    print(f"Only Alice has: {achievements_set.intersection(alice)}")
    print(f"Only Bob has: {achievements_set.intersection(bob)}")
    print(f"Only Charlie has: {achievements_set.intersection(charlie)}")
    print(f"Only Dylan has: {achievements_set.intersection(dylan)}\n")
    print(f"Alice is missing: {achievements_set.difference(alice)}")
    print(f"Bob is missing: {achievements_set.difference(bob)}")
    print(f"Charlie is missing: {achievements_set.difference(charlie)}")
    print(f"Dylan is missing: {achievements_set.difference(dylan)}")


if __name__ == "__main__":
    gen_player_achievements()
