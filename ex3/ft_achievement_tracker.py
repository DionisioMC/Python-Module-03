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
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}\n")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")
    print(f"Alice is missing: {achievements_set.difference(alice)}\n")
    print(f"Bob is missing: {achievements_set.difference(bob)}\n")
    print(f"Charlie is missing: {achievements_set.difference(charlie)}\n")
    print(f"Dylan is missing: {achievements_set.difference(dylan)}\n")


if __name__ == "__main__":
    gen_player_achievements()
