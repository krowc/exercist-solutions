"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for key, value in inventory.items():
        if key == None or value == 0:
            continue

        count = value
        while count > 0:
            items.append(key)  
            count -= 1

    return create_inventory(items)
    

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for entry in items:
        if entry in inventory:
            if inventory[entry] > 0:
                inventory[entry] -= 1
    # EYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    return inventory
    
    #1: Check if items[i] is in inventory
    #    if yes: check if item val in inventory == 0
    #        if yes: skip
    #        if  no: decrement
    #    if  no: skip
    #    /Pseudocode wins the day/.


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
        
    return inventory
    


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    available_inventory = []
    for key, value in inventory.items():
        if value > 0:
            available_inventory.append((key, value))

    return available_inventory