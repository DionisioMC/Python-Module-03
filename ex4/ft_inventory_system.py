import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")
        items: dict[str, int] = {}
        for item in sys.argv[1:]:
            inventory_item = item.split(":")
            try:
                if len(inventory_item) != 2:
                    print(f"Error - invalid parameter '{item}'")
                elif inventory_item[0] in items.keys():
                    print(f"Redundant item '{inventory_item[0]}' - discarding")
                else:
                    items.update({inventory_item[0]: int(inventory_item[1])})
            except Exception as e:
                print(f"Quantity error for '{inventory_item[0]}': {e}")
        print(f"Got inventory: {items}")
        print(f"Item list: {list(items.keys())}")
        length = len(items.keys())
        total = sum(items.values())
        print(f"Total quantity of the {length} items: {sum(items.values())}")
        for item, num in items.items():
            print(f"Item {item} represents {round((num / total) * 100, 1)}%")
        first = (list(items.keys())[0], list(items.values())[0])
        maximum: tuple[str, int] = first
        minimum: tuple[str, int] = first
        for game_item in items.keys():
            if maximum[1] < items[game_item]:
                maximum = (game_item, items[game_item])
            elif minimum[1] > items[game_item]:
                minimum = (game_item, items[game_item])
        print(f"Item most abundant: {maximum[0]} with quantity {maximum[1]}")
        print(f"Item least abundant: {minimum[0]} with quantity {minimum[1]}")
        items.update({"magic_item": 1})
        print(items)
    else:
        print("No items provided. Usage: "
              "python3 ft_inventory_systems.py "
              "<item1>:quantity <item2>:quantity ...")
