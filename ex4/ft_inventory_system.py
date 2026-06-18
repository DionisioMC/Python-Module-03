import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")
        items: dict[str, int] = {}
        for item in sys.argv[1:]:
            inventory_item = item.split(":")
            try:
                if inventory_item[0] == item:
                    print(f"Error - invalid parameter '{item}'")
                elif inventory_item[0] in items.keys():
                    print(f"Redundant item '{inventory_item[0]}' - discarding")
                else:
                    items.update({inventory_item[0]: int(inventory_item[1])})
            except Exception as e:
                print(f"Quantity error for '{inventory_item[0]}': {e}")
        print(items)
        length = len(items.keys())
        total = sum(items.values())
        print(f"Total quantity of the {length} items: {sum(items.values())}")
        for item, num in items.items():
            print(f"Item {item} represents {round((num / total) * 100, 1)}%")
        maximum: tuple[str, int] = list(items.items())[0]
        minimum: tuple[str, int] = list(items.items())[0]
        for game_item in items.items():
            if maximum[1] < game_item[1]:
                maximum = game_item
            elif minimum[1] > game_item[1]:
                minimum = game_item
        print(f"Item most abundant: {maximum[0]} with quantity {maximum[1]}")
        print(f"Item least abundant: {minimum[0]} with quantity {minimum[1]}")
        items.update({"magic_item": 1})
        print(items)
    else:
        print("No items provided. Usage: python3 ft_inventory_systems.py <item1>:quantity <item2>:quantity ...")
