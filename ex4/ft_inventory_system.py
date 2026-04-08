import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        if ":" not in arg or arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str
        quantity: str
        item, quantity = arg.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            value = int(quantity)
            if value < 0:
                continue
            inventory[item] = value
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")

    item_list: list[str] = list(inventory.keys())
    if len(item_list) == 0:
        return

    first_item: str = item_list[0]
    most_abundant: str = first_item
    max_quantity: int = inventory[first_item]
    lest_abundant: str = first_item
    min_quantity: int = inventory[first_item]

    for item in item_list:
        print(f"Item '{item}' represents "
              f"{round(inventory[item] / sum(inventory.values()) * 100, 1)}%")

        if inventory[item] > max_quantity:
            max_quantity = inventory[item]
            most_abundant = item

        if inventory[item] < min_quantity:
            min_quantity = inventory[item]
            lest_abundant = item

    print(f"Item most abundant: {most_abundant} with quantity "
          f"{inventory[most_abundant]}")
    print(f"Item least abundant: {lest_abundant} with quantity "
          f"{inventory[lest_abundant]}")

    inventory.update({"potion": 3})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
