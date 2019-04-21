import engine
import pygame

class LifeBar:
    """É a barra de HP dos lutadores"""
    def __init__(self,fighterName = "Scorpion"):
        self.hp = 100
        self.damage = 0
        self.lifeBarImg = pygame.image.load('../res/' + fighterName + 'lifebar.png')
        self.damageFull = pygame.image.load('../res/DamageFull.png')
        self.shown = self.damage/100.0
        self.damageImage = pygame.transform.chop(self.damageFull,(0.0, 0.0, self.shown, 1.0))
        #self.lifeBarImg = engine.Image('../res/' + fighterName + 'lifebar')
        #self.damageFull = engine.Image('../res/DamageFull')
        self.unitWidth = self.lifeUnit.getWidth()
        self.pos = [0.0, 0.0]
        self.RelativePos = [[168,-21],[4,-21]]"Posição da barra de hp relativa(cheia)"
        self.initialPos = []
        self.dmgPos = self.RelativePos[0]

    def addDamage(self,dmg):
        """Adciona dano ao hp do personagem,se quizer curar basta um numero inteiro negativo"""
        self.hp = self.hp - dmg
        self.damage = self.damage + dmg
        self.shown = self.damage/100.0
        self.damageImage = pygame.transform.chop(self.damageFull, (0.0, 0.0, self.shown, 1.0))
        self.__damagePosition()
    def getDamage(self):
        """Retorna o dano já sofrido pelo personagem"""
        return self.damage
    def returnLife(self):
        """retorna o life para '100' e damage para '0'"""
        self.hp = 100
        self.damage = 0

    def getLife(self):
        """Retorna o hp do personagem"""
        return self.hp

    def isDead(self):
        """Verifica se HP é menor ou igual a zero"""
        if self.hp <=0 :
            return True
        return False

    def setLifePosition(self,pos = [0.0,0.0]):
        self.pos = pos

    def __damagePosition(self):
        """abstract"""

    def render(self):
       pygame.Surface.blit(self.lifeBarImg,(self.pos[0],self.pos[1]))
       pygame.Surface.blit(self.damageImage, (self.pos[0] + self.dmgPos[0], self.pos[1]+self.dmgPos[1]))

class Player1LifeBar(LifeBar):
    def __init__(self,fighterName = "Scorpion"):
        LifeBar.__init__(self,fighterName)
        self.initialPos = self.RelativePos[0]
        self.dmgPos = self.initialPos

    def __damagePosition(self):
        """abstract"""
        self.dmgPos = [self.initialPos[1] - self.damageImage.get_width(),self.initialPos[1]]

class Player2LifeBar(LifeBar):
    def __init__(self,fighterName = "Scorpion"):
        LifeBar.__init__(self,fighterName)
        self.initialPos = self.RelativePos[1]
        self.dmgPos = self.initialPos

    def __damagePosition(self):
        """abstract"""

