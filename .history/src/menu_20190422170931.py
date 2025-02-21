import pygame
import os
from pygame.locals import *
import config
import game
import engine
import fightScene


class Menu:
    pass

class MainMenu(Menu):
    def __init__(self, game=engine.Game()):
        clock = pygame.time.Clock()
        screen = "start"
        mainmenu = pygame.image.load('../res/Background/MainMenu01.png')
        game.getDisplay().blit(mainmenu, (0, 0))
        pygame.display.update()
        while True:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    # carregar áudio   
                    sound = engine.Sound()
                    if event.key == 8: # 8 == backspace
                        pygame.quit()
                    if event.key == 13:  # 13 == ENTER
                        # coloca áudio "in"
                        if screen == "start":
                            sound.setSound("start")
                            sound.play()
                            ScenarioMenu()
                        if screen == "options":
                            sound.setSound("options")
                            sound.play()                            
                            OptionMenu()
                    elif screen == "start":
                        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                            sound.play()                              
                            screen = "options"
                            mainmenu = pygame.image.load(
                                '../res/Background/MainMenu02.png')
                            game.getDisplay().blit(mainmenu, (0, 0))
                            pygame.display.update()

                    elif screen == "options":                          
                        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                            sound.play()
                            screen = "start"                           
                            mainmenu = pygame.image.load(
                                '../res/Background/MainMenu01.png')
                            game.getDisplay().blit(mainmenu, (0, 0))
                            pygame.display.update()


class OptionMenu(Menu):
    def __init__(self, game=engine.Game()):
        mainmenu = pygame.image.load('../res/Background/Instrucoes.png')
        game.getDisplay().blit(mainmenu, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        # colocar áudio "out"
                        sound = engine.Sound("back")
                        sound.play()     
                        MainMenu()


class CharMenu(Menu):
    pass


class ScenarioMenu(Menu):
    def __init__(self, game=engine.Game()):
        scenario = 1  # {1,2,3,4,5,6,7,8,9=random}
        self.mainmenu = pygame.image.load('../res/Background/ChoosingScenario/ChooseScenario01.png')
        self.game = game
        game.getDisplay().blit(self.mainmenu, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                # carregar áudio
                sound = engine.Sound() 
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:  # 13 == ENTER
                        # Entra no cenário escolhido
                        sound.setSound("fight")
                        sound.play()
                        fight = fightScene.Scenario(game,scenario)
                        fight.setScenario(scenario)
                    elif scenario == 1:
                        if event.key == pygame.K_DOWN:
                            sound.play()
                            scenario = 4
                        if event.key == pygame.K_RIGHT:
                            sound.play()                            
                            scenario = 2

                        self.setScenario(scenario)

                    elif scenario == 2:
                        if event.key == pygame.K_DOWN:
                            sound.play()
                            scenario = 5
                        if event.key == pygame.K_RIGHT:
                            sound.play()
                            scenario = 3
                        if event.key == pygame.K_LEFT:
                            sound.play()
                            scenario = 1
                        self.setScenario(scenario)

                    elif scenario == 3:
                        if event.key == pygame.K_DOWN:
                            sound.play()
                            scenario = 6
                        if event.key == pygame.K_LEFT:
                            sound.play()
                            scenario = 2
                        self.setScenario(scenario)

                    elif scenario == 4:
                        if event.key == pygame.K_DOWN:
                            sound.play()
                            scenario = 7
                        if event.key == pygame.K_RIGHT:
                            sound.play()
                            scenario = 5
                        if event.key == pygame.K_UP:
                            sound.play()
                            scenario = 1
                        self.setScenario(scenario)

                    elif scenario == 5:
                        if event.key == pygame.K_DOWN:
                            sound.play()
                            scenario = 8
                        if event.key == pygame.K_RIGHT:
                            sound.play()
                            scenario = 6
                        if event.key == pygame.K_LEFT:
                            sound.play()
                            scenario = 4
                        if event.key == pygame.K_UP:
                            sound.play()
                            scenario = 2
                        self.setScenario(scenario)

                    elif scenario == 6:
                        if event.key == pygame.K_DOWN:
                            sound.play()
                            scenario = 9
                        if event.key == pygame.K_LEFT:
                            sound.play()
                            scenario = 5
                        if event.key == pygame.K_UP:
                            sound.play()
                            scenario = 3
                        self.setScenario(scenario)

                    elif scenario == 7:
                        if event.key == pygame.K_RIGHT:
                            sound.play()
                            scenario = 8
                        if event.key == pygame.K_UP:
                            sound.play()
                            scenario = 4
                        self.setScenario(scenario)

                    elif scenario == 8:
                        if event.key == pygame.K_RIGHT:
                            sound.play()
                            scenario = 9
                        if event.key == pygame.K_LEFT:
                            sound.play()
                            scenario = 7
                        if event.key == pygame.K_UP:
                            sound.play()
                            scenario = 5
                        self.setScenario(scenario)

                    elif scenario == 9: 
                        if event.key == pygame.K_LEFT:
                            sound.play()
                            scenario = 8
                        if event.key == pygame.K_UP:
                            sound.play()
                            scenario = 6
                        self.setScenario(scenario)

                    if event.key == pygame.K_ESCAPE:
                        # colocar áudio "out"
                        sound = engine.Sound("back")
                        sound.play()     
                        MainMenu()

    def setScenario(self, scenario):
        self.mainmenu = pygame.image.load('../res/Background/ChoosingScenario/ChooseScenario0'+str(scenario)+'.png')
        self.game.getDisplay().blit(self.mainmenu, (0, 0))
        pygame.display.update()
