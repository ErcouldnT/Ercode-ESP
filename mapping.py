"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""


ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "Yakın Sloop",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "Yakın Brig",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "Yakın Galleon",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Galleon",
    },

    "BP_AISmallShipTemplate_C": {
        "Name": "Yakın İskelet Sloop",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "İskelet Sloop",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "Yakın İskelet Galleon",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "İskelet Galleon",
    },
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}

items = {
    "BP_EmissaryFlotsam_OrderOfSouls_Rank5_ItemInfo_C": {
        "Name": "Order 5",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank4_ItemInfo_C": {
        "Name": "Order 4",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank3_ItemInfo_C": {
        "Name": "Order 3",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank2_ItemInfo_C": {
        "Name": "Order 2",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank1_ItemInfo_C": {
        "Name": "Order 1",
    },

    "BP_EmissaryFlotsam_GoldHoarders_Rank5_ItemInfo_C": {
        "Name": "Gold 5",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank4_ItemInfo_C": {
        "Name": "Gold 4",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank3_ItemInfo_C": {
        "Name": "Gold 3",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank2_ItemInfo_C": {
        "Name": "Gold 2",
    },
    "BP_EmissaryFlotsam_GoldHoarders_ItemInfo_C": {
        "Name": "Gold 1",
    },

    "BP_EmissaryFlotsam_Reapers_Rank5_ItemInfo_C": {
        "Name": "Reaper 5",
    },
    "BP_EmissaryFlotsam_Reapers_Rank4_ItemInfo_C": {
        "Name": "Reaper 4",
    },
    "BP_EmissaryFlotsam_Reapers_Rank3_ItemInfo_C": {
        "Name": "Reaper 3",
    },
    "BP_EmissaryFlotsam_Reapers_Rank2_ItemInfo_C": {
        "Name": "Reaper 2",
    },
    "BP_EmissaryFlotsam_Reapers_ItemInfo_C": {
        "Name": "Reaper 1",
    },

    "BP_EmissaryFlotsam_AthenasFortune_Rank5_ItemInfo_C": {
        "Name": "Athena 5",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank4_ItemInfo_C": {
        "Name": "Athena 4",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank3_ItemInfo_C": {
        "Name": "Athena 3",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank2_ItemInfo_C": {
        "Name": "Athena 2",
    },
    "BP_EmissaryFlotsam_AthenasFortune_ItemInfo_C": {
        "Name": "Athena 1",
    },

    "BP_EmissaryFlotsam_MerchantAlliance_Rank5_ItemInfo_C": {
        "Name": "Merchant 5",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank4_ItemInfo_C": {
        "Name": "Merchant 4",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank3_ItemInfo_C": {
        "Name": "Merchant 3",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank2_ItemInfo_C": {
        "Name": "Merchant 2",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_ItemInfo_C": {
        "Name": "Merchant 1",
    },

    "BP_Rowboat_C": {
        "Name": "Rowboat",
    },
    "BP_Rowboat_WithFrontHarpoon_C": {
        "Name": "Harpoon Rowboat",
    },
    "BP_SwampRowboat_C": {
        "Name": "Swamp Rowboat",
    },

    "BP_MerchantCrate_BigGunpowderBarrel_ItemInfo_C": {
        "Name": "Big Keg",
    },
    "BP_MerchantCrate_GunpowderBarrel_ItemInfo_C": {
        "Name": "Keg",
    },
    "BP_MerchantCrate_PirateLegendBigGunpowderBarrel_ItemInfo_C": {
        "Name": "Athena keg",
    },
    
    "BP_TreasureChest_ItemInfo_PirateLegend_C": {
        "Name": "LEGENDARY CHEST",
    },
    "BP_AshenWindsSkull_ItemInfo_C": {
        "Name": "ASHEN SKULL",
    },

    "BP_LegendaryFort_StrongholdKey_ItemInfo_C": {
        "Name": "FoF Key",
    },

    "BP_PlayerPirate_C": {
        "Name": "Adam",
    },
}

ship_keys = set(ships.keys())
item_keys = set(items.keys())
