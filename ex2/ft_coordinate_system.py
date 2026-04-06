import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinate: str = ""
        try:
            values: str = input("Enter new coordinates as floats in "
                                "format 'x, y, z': ")
            if values.count(",") != 2:
                print("Invalid syntax")
                continue
            coordinates: list[str] = values.split(",")
            final_coordinates: list[float] = []
            for coordinate in coordinates:
                final_coordinates = final_coordinates + [float(
                    coordinate.strip())]
            x, y, z = final_coordinates
            return (x, y, z)
        except ValueError as error:
            print(f"Error on parameter '{coordinate}': {error}")


def calculate_distance(first_pos: tuple[float, float, float],
                       second_pos: tuple[float, float, float]) -> float:
    x1, y1, z1 = first_pos
    x2, y2, z2 = second_pos
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_pos: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")
    print(f"Distance to center: "
          f"{calculate_distance(first_pos, (0.0, 0.0, 0.0))}\n")

    print("Get a second set of coordinates")
    second_pos: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of "
          f"coordinates: {calculate_distance(first_pos, second_pos)}")


if __name__ == "__main__":
    main()
