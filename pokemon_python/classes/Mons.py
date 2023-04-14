import Types
import Moves

global pokedex
pokedex = {}

class Mons:
    
    def __init__(self, monID, name, type, level, hp, atk, defense, speed, moveset):
        self.monID = monID
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.speed = speed
        self.moveset = moveset


    def getMonID(self):
        return self.monID
    
    def getName(self):
        return self.name
    
    def getType(self):

        try: 
            if len(self.type) > 1:
                return self.type[0].getTypeStr() + "/" + self.type[1].getTypeStr()
            else:
                return self.type[0].getTypeStr()
        except:
            return self.type.getTypeStr()    
            
    def getLevel(self):
        return self.level
    
    def getHP(self):
        return self.hp
    
    def getAtk(self):
        return self.atk
    
    def getDefense(self):
        return self.defense
    
    def getSpeed(self):
        return self.speed
    
    def getMoveset(self):
        moveoutput = "| "

        for move in self.moveset:
            moveoutput += move.getName() + " | "
        
        return moveoutput
    
    def printMon(self):
        print()
        print("Name: " + self.name)
        print("Type: " + self.getType())
        print("Level: " + str(self.level))
        print("HP: " + str(self.hp))
        print("Attack: " + str(self.atk))
        print("Defense: " + str(self.defense))
        print("Speed: " + str(self.speed))
        print("Moveset: " + self.getMoveset()) 
        print()

class Bulbasaur(Mons):
        
        def __init__(self):
            super().__init__(0, "Bulbasaur", [Types.Grass(), Types.Poison()], 5, 45, 49, 49, 45, [Moves.Tackle(), Moves.VineWhip(), Moves.RazorLeaf()])

class Charmander(Mons):
            
            def __init__(self):
                super().__init__(1, "Charmander", Types.Fire(), 5, 39, 52, 43, 65, [Moves.Scratch(), Moves.Ember()])

class Squirtle(Mons):
                    
            def __init__(self):
                super().__init__(2, "Squirtle", Types.Water(), 5, 44, 48, 65, 43, [Moves.Tackle(), Moves.WaterGun()])

class Pikachu(Mons):
                        
            def __init__(self):
                super().__init__(3, "Pikachu", Types.Electric(), 5, 35, 55, 40, 90, [Moves.Tackle(), Moves.ThunderShock()])


def createStarters():
    starters = [Bulbasaur(), Charmander(), Squirtle(), Pikachu()]
    for i in starters:
        pokedex[i.monID] = i

    pass

def main():
    createStarters()
    
    for mon in pokedex:
        pokedex[mon].printMon()

if __name__ == "__main__":
      main()