import math


def get_player_pos() -> tuple[float, float, float]:
    coords: list[float] = []
    while len(coords) != 3:
        coords = []
        raw_coord: list[str] = []
        raw: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        raw_coord = raw.split(",")
        if raw == raw_coord[0]:
            print("Invalid syntax")
        else:
            try:
                for coord in raw_coord:
                    coords.append(float(coord.strip()))
            except ValueError as e:
                print(f"Error on parameter '{coord.strip()}': {e}")
    return (coords[0], coords[1], coords[2])


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: ({first[0]}, {first[1]}, {first[2]})")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    distance = math.sqrt((first[0] ** 2) + (first[1] ** 2) + (first[2] ** 2))
    print(f"Distance to center: {round(distance, 4)}\n")
    print("Get a second set of coordinates")
    second = get_player_pos()
    distance = math.sqrt(((first[0] - second[0]) ** 2) +
                         ((first[1] - second[1]) ** 2) +
                         ((first[2] - second[2]) ** 2))
    print(
        f"Distance between the 2 sets of coordinates: {round(distance, 4)}\n")
