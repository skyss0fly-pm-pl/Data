class Cobblestone:
    def __init__(self):
        self.id = "minecraft:cobblestone"
        self.hardness = 0.7
        self.stack = 64
        self.placeability = "all"
        self.light = 0
        self.gravity = False
        self.sound = "dig.stone"
        self.blast_resistance = 0
        self.flammable = False
        self.slipperiness = 0.6
        self.solid = True
        self.transparent = False
        self.harvest_tool = "pickaxe"
        self.harvest_material = "hand"
        self.height = 1
        self.width = 1
        self.length = 1
        self.xp_range = (0,0)
        self.drop = {
            "minecraft:cobblestone": 100
        }
