import Types

global movelist
movelist = {}

class Moves:

    def __init__(self, moveID, name, type, power, accuracy, pp):
        self.moveID = moveID
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
    
    def getMoveID(self):
        return self.moveID
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type.getTypeStr()
    
    def getPower(self):
        return self.power
    
    def getAccuracy(self):
        return self.accuracy
    
    def getPP(self):
        return self.pp
    

class Tackle(Moves):
        
        def __init__(self):
            super().__init__(0, "Tackle", Types.Normal(), 40, 100, 35)

class VineWhip(Moves):
            
        def __init__(self):
            super().__init__(1, "Vine Whip", Types.Grass(), 45, 100, 25)

class WaterGun(Moves):
                    
        def __init__(self):
            super().__init__(2, "Water Gun", Types.Water(), 40, 100, 25)

class Ember(Moves):
      
        def __init__(self):
            super().__init__(3, "Ember", Types.Fire(), 40, 100, 25)

class RazorLeaf(Moves):
      
        def __init__(self):
            super().__init__(4, "Razor Leaf", Types.Grass(), 55, 95, 25)

class Bubble(Moves):
      
        def __init__(self):
            super().__init__(5, "Bubble", Types.Water(), 40, 100, 30)

class FireFang(Moves):
      
        def __init__(self):
            super().__init__(6, "Fire Fang", Types.Fire(), 65, 95, 15)

class ThunderShock(Moves):
      
        def __init__(self):
            super().__init__(7, "Thunder Shock", Types.Electric(), 40, 100, 30)

class Confusion(Moves):
      
        def __init__(self):
            super().__init__(8, "Confusion", Types.Psychic(), 50, 100, 25)

class IceShard(Moves):
      
        def __init__(self):
            super().__init__(9, "Ice Shard", Types.Ice(), 40, 100, 30)

class DragonRage(Moves):
        
        def __init__(self):
            super().__init__(10, "Dragon Rage", Types.Dragon(), 0, 100, 10)

class DarkPulse(Moves):
          
        def __init__(self):
            super().__init__(11, "Dark Pulse", Types.Dark(), 80, 100, 15)

class SteelWing(Moves):
          
        def __init__(self):
            super().__init__(12, "Steel Wing", Types.Steel(), 70, 90, 25)

class NightSlash(Moves):
          
        def __init__(self):
            super().__init__(13, "Night Slash", Types.Dark(), 70, 100, 15)

class FairyWind(Moves):
          
        def __init__(self):
            super().__init__(14, "Fairy Wind", Types.Fairy(), 40, 100, 30)

class Scratch(Moves):
          
        def __init__(self):
            super().__init__(15, "Scratch", Types.Normal(), 40, 100, 35)

class Bite(Moves):
          
        def __init__(self):
            super().__init__(16, "Bite", Types.Dark(), 60, 100, 25)


def createMoves():
    movelist[0] = Tackle()
    movelist[1] = VineWhip()
    movelist[2] = WaterGun()
    movelist[3] = Ember()
    movelist[4] = RazorLeaf()
    movelist[5] = Bubble()
    movelist[6] = FireFang()
    movelist[7] = ThunderShock()
    movelist[8] = Confusion()
    movelist[9] = IceShard()
    movelist[10] = DragonRage()
    movelist[11] = DarkPulse()
    movelist[12] = SteelWing()
    movelist[13] = NightSlash()
    movelist[14] = FairyWind()
    movelist[15] = Scratch()
    movelist[16] = Bite()
    
    
