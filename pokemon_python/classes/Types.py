class Type:

    def __init__(self, typeID, typeStr, weaknesses, resistances, immunities):
        self.typeID = typeID
        self.typeStr = typeStr
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities

    def getTypeID(self):
        return self.typeID
    
    def getTypeStr(self):
        return str(self.typeStr)
        
    def getWeaknesses(self):
        return self.weaknesses
    
    def getResistances(self):
        return self.resistances
    
    def getImmunities(self):
        return self.immunities
    
class Water(Type):

    def __init__(self):
        super().__init__(0, "Water", [Electric, Grass], [Fire, Water, Ice, Steel], [])
    
class Fire(Type):

    def __init__(self):
        super().__init__(1, "Fire", [Ground, Rock, Water], [Fire, Bug, Grass, Ice, Steel], [])

class Grass(Type):

    def __init__(self):
        super().__init__(2, "Grass", [Fire, Flying, Bug, Ice], [Electric, Grass, Ground, Water], [])

class Normal(Type):
    
    def __init__(self):
        super().__init__(3, "Normal", [Fighting], [Ghost], [Ghost])

class Flying(Type):
    
    def __init__(self):
        super().__init__(4, "Flying", [Electric, Rock, Ice], [Fighting, Bug, Grass], [Ground])

class Poison(Type):
    
    def __init__(self):
        super().__init__(5, "Poison", [Ground, Psychic], [Bug, Fighting, Grass, Poison], [])

class Ground(Type):
    
    def __init__(self):
        super().__init__(6, "Ground", [Water, Grass, Ice], [Poison, Rock], [Electric])

class Rock(Type):
    
    def __init__(self):
        super().__init__(7, "Rock", [Fighting, Grass, Ground, Steel, Water], [Fire, Flying, Normal, Poison], [])

class Bug(Type):
    
    def __init__(self):
        super().__init__(8, "Bug", [Fire, Flying, Rock], [Fighting, Grass, Ground], [])

class Ghost(Type):
    
    def __init__(self):
        super().__init__(9, "Ghost", [Dark, Ghost], [Bug, Poison], [Normal, Fighting])

class Electric(Type):
    
    def __init__(self):
        super().__init__(10, "Electric", [Ground], [Electric, Flying, Steel], [])

class Psychic(Type):
    
    def __init__(self):
        super().__init__(11, "Psychic", [Bug, Dark, Ghost], [Fighting, Psychic], [])

class Ice(Type):
    
    def __init__(self):
        super().__init__(12, "Ice", [Fire, Fighting, Rock, Steel, Water], [Ice], [])

class Dragon(Type):
    
    def __init__(self):
        super().__init__(13, "Dragon", [Dragon, Ice, Fairy], [Electric, Fire, Grass, Water], [])

class Dark(Type):
    
    def __init__(self):
        super().__init__(14, "Dark", [Bug, Fighting, Fairy], [Ghost, Dark], [Psychic])

class Steel(Type):  
    
    def __init__(self):
        super().__init__(15, "Steel", [Fire, Fighting, Ground], [Bug, Dark, Dragon, Flying, Ghost, Grass, Ice, Normal, Psychic, Rock, Steel], [Poison])

class Fairy(Type):
        
    def __init__(self):
        super().__init__(16, "Fairy", [Bug, Dark, Fighting], [Poison, Steel], [Dragon])

class Fighting(Type):
    
    def __init__(self):
        super().__init__(17, "Fighting", [Flying, Psychic, Fairy], [Bug, Dark, Rock], [])

