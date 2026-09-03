from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresCamera(multiworld: MultiWorld, player: int, camera: str):
    """Gets the camera needed in logic and spits out the correct requires string for each camera split option."""
    from ..Helpers import get_option_value

    if get_option_value(multiworld, player, "split_cameras") == 0:
        return None
    elif get_option_value(multiworld, player, "split_cameras") == 2:
        camera = "|" + camera + " Camera|"
        return camera
    else:
        if "Hall" in camera:
            return "|Halls|"
        elif camera == "Storage" or camera == "Right Vent":
            return "|Storage + Right Vent|"
        elif camera == "Kitchen" or camera == "Entrance":
            camera = "|" + camera + "|"
            return camera
        elif camera == "Maintenance" or camera == "Left Vent":
            return "|Maintenance + Left Vent|"
        elif camera == "Arcade" or camera == "Prize Corner":
            return "|Arcade + Prize Corner|"
        elif camera == "Dining Room" or camera == "Stage" or camera == "Backstage":
            return "|Dining Room + Stage + Backstage|"
        else:
            return "Error"
