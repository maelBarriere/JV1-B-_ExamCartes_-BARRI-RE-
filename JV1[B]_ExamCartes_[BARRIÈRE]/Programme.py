class Cartes:
    def __init__(self,mana,name,description):
        self.__mana = mana
        self.__name = name
        self.__description = description
    def getMana(self): 
        return self.__mana
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description

class Mage:
    def __init__(self,name,pv,total,actualmana,main,défausse,zone,creature):
        self.__name = name
        self.__pv = 100
        self.__total = 50
        self.__actualmana = 120
        self.__main = main
        self.__défausse = défausse
        self.__zone = zone
        self.__creature = creature
    def getName(self):
        return self.__name
    def getPv(self):
        return self.__pv
    def getTotal(self):
         return self.__total
    def getActualMana(self):
         return self.__actualmana
    def getMain(self):
         return self.__main
    def getDéfausse(self):
           return self.__défausse
    def getZone(self):
           return self.__zone
    def getCreature(self):
          return self.__creature
        if autreMage != jouer :
            Mage =+ mana
class Cristal(Cartes):
       def __init__(self,valeur):
          Cartes.__init__(self,valeur)
          self.__valeur = valeur 
       def getValeur(self):
          return self.__valeur

class Creature(Cartes):
       def __init__(self,pv,atk):
              Cartes.__init__(self,pv,atk)
       def getPv(self):
          return self.__pv
       def getAtk(self):
          return self.__atk
       
class Blast(Cartes):
       def __init__(self,valeur):
              Cartes.__init__(self,valeur)
       def getValeur(self):
            return self.__valeur

           
           
    