from Types import Electric
from Types import Psychic
from Types import Ice
from Types import Dragon
from Types import Dark
from Types import Steel
from Types import Fairy
from Types import Fighting
from Types import Grass
from Types import Normal
from Types import Flying
from Types import Poison
from Types import Ground
from Types import Rock
from Types import Bug
from Types import Ghost
from Types import Fire
from Types import Water

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
            super().__init__(0, "Tackle", Normal(), 40, 100, 35)

class VineWhip(Moves):
            
        def __init__(self):
            super().__init__(1, "Vine Whip", Grass(), 45, 100, 25)

class WaterGun(Moves):
                    
        def __init__(self):
            super().__init__(2, "Water Gun", Water(), 40, 100, 25)

class Ember(Moves):
      
        def __init__(self):
            super().__init__(3, "Ember", Fire(), 40, 100, 25)

class RazorLeaf(Moves):
      
        def __init__(self):
            super().__init__(4, "Razor Leaf", Grass(), 55, 95, 25)

class Bubble(Moves):
      
        def __init__(self):
            super().__init__(5, "Bubble", Water(), 40, 100, 30)

class FireFang(Moves):
      
        def __init__(self):
            super().__init__(6, "Fire Fang", Fire(), 65, 95, 15)

class ThunderShock(Moves):
      
        def __init__(self):
            super().__init__(7, "Thunder Shock", Electric(), 40, 100, 30)

class Confusion(Moves):
      
        def __init__(self):
            super().__init__(8, "Confusion", Psychic(), 50, 100, 25)

class IceShard(Moves):
      
        def __init__(self):
            super().__init__(9, "Ice Shard", Ice(), 40, 100, 30)

class DragonRage(Moves):
        
        def __init__(self):
            super().__init__(10, "Dragon Rage", Dragon(), 0, 100, 10)

class DarkPulse(Moves):
          
        def __init__(self):
            super().__init__(11, "Dark Pulse", Dark(), 80, 100, 15)

class SteelWing(Moves):
          
        def __init__(self):
            super().__init__(12, "Steel Wing", Steel(), 70, 90, 25)

class NightSlash(Moves):
          
        def __init__(self):
            super().__init__(13, "Night Slash", Dark(), 70, 100, 15)

class FairyWind(Moves):
          
        def __init__(self):
            super().__init__(14, "Fairy Wind", Fairy(), 40, 100, 30)

class Scratch(Moves):
          
        def __init__(self):
            super().__init__(15, "Scratch", Normal(), 40, 100, 35)

class Bite(Moves):
          
        def __init__(self):
            super().__init__(16, "Bite", Dark(), 60, 100, 25)


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
    
    
