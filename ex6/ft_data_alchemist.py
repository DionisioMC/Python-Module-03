import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    player_list = ['Alice', 'bob', 'Charlie', 'dylan',
                   'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {player_list}")
    capitalized_list = [player.capitalize() for player in player_list]
    print(f"New list with all names capitalized: {capitalized_list}")
    filtered_list = [ele for ele in player_list if ele == ele.capitalize()]
    print(f"New list of capitalized names only: {filtered_list}")
    scores = {player: round(random.random() * 1000)
              for player in capitalized_list}
    print(f"Score dict: {scores}")
    values = [scores[score] for score in scores]
    average = round(sum(values) / len(values), 2)
    print(f"Score average is {average}")
    high_scores = {player: scores[player] for player in scores if scores[player] > average}
    print(f"High scores: {high_scores}")
