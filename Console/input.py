import pygame

class InputManager:
    def __init__(self):
        self.left = False
        self.right = False
        self.select = False
        self.back = False

        self.cooldown = 0

    def update(self, events):
        self.left = False
        self.right = False
        self.select = False
        self.back = False

        if self.cooldown > 0:
            self.cooldown -= 1

        for event in events:

            # 🎹 CLAVIER
            if event.type == pygame.KEYDOWN and self.cooldown == 0:
                if event.key == pygame.K_LEFT:
                    self.left = True
                    self.cooldown = 10

                if event.key == pygame.K_RIGHT:
                    self.right = True
                    self.cooldown = 10

                if event.key == pygame.K_RETURN:
                    self.select = True

            # 🎮 D-PAD
            if event.type == pygame.JOYHATMOTION and self.cooldown == 0:
                x, y = event.value

                if x == 1:
                    self.right = True
                    self.cooldown = 10

                if x == -1:
                    self.left = True
                    self.cooldown = 10

            # 🎮 BOUTONS
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # A (Xbox) / X (PlayStation)
                    self.select = True
                if event.button == 1:
                    self.back = True

            # 🎮 STICK ANALOGIQUE
            if event.type == pygame.JOYAXISMOTION and self.cooldown == 0:
                if event.axis == 0:  # axe horizontal
                    if event.value > 0.6:
                        self.right = True
                        self.cooldown = 10
                    elif event.value < -0.6:
                        self.left = True
                        self.cooldown = 10