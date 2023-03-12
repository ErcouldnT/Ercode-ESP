"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Yakın)",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "Brig (Yakın)",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "Galleon (Yakın)",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Galleon",
    },

    "BP_AISmallShipTemplate_C": {
        "Name": "Skeleton Sloop (Yakın)",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "Skeleton Sloop",
    },

    "BP_AILargeShipTemplate_C": {
        "Name": "Skeleton Galleon (Yakın)",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Skeleton Galleon",
    },
    
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}

ship_keys = set(ships.keys())
# skeleton_ship_keys = set(skeleton_ships.keys())
