"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart.setdefault(item, 1)

    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shop_cart = {}

    for item in notes:
        shop_cart.setdefault(item, 1)

    return shop_cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(dict(recipe_updates))
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}

    for item in cart.keys():
        fulfillment_cart[item] = [cart[item]] + aisle_mapping[item]

    fulfillment_cart = dict(sorted(fulfillment_cart.items(), reverse=True))
    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_inventory = {}
    for key, value in store_inventory.items(): # store inventory can contain more items than cart
        if key not in fulfillment_cart:
            updated_inventory[key] = store_inventory[key]
            continue
            
        updated_inventory[key] = [store_inventory[key][0] - fulfillment_cart[key][0]]
        updated_inventory[key] += store_inventory[key][1:]

        if updated_inventory[key][0] == 0:
            updated_inventory[key][0] = 'Out of Stock'

# Called update_store_inventory(
#     param: {'Kiwi': [3, 'Aisle 6', False]},
#     param: {'Kiwi': [3, 'Aisle 6', False], 'Juice': [5, 'Aisle 5', False], 'Yoghurt': [2, 'Aisle 2', True], 'Milk': [5, 'Aisle 2', True]}). 

# The function returned {'Kiwi': ['Out of Stock', 'Aisle 6', False]}, 

# but the tests expected: {'Juice': [5, 'Aisle 5', False], 'Yoghurt': [2, 'Aisle 2', True], 'Milk': [5, 'Aisle 2', True], 'Kiwi': ['Out of Stock', 'Aisle 6', False]} as the store inventory.

        
    return updated_inventory
