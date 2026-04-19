import pygame, subprocess
from store import fetch_games, download_game

class Launcher:
    def __init__(self):
        self.games = [
            {"name": "Store", "type": "store", "file":None},
            {"name": "Rogue I", "file": "games/rogue/main.py"},
            {"name": "Ako Tower", "file": "games/ako_tower/main.py"},
        ]

        self.index = 0
        self.scroll_x = 0

        self.font = pygame.font.Font(None, 50)
        self.big_font = pygame.font.Font(None, 80)

    def update(self, input_manager):
        if input_manager.right:
            self.index = (self.index + 1) % len(self.games)

        if input_manager.left:
            self.index = (self.index - 1) % len(self.games)

        if input_manager.select:
            self.launch()

        target_x = self.index * 300
        self.scroll_x += (target_x - self.scroll_x) * 0.12

    def launch(self):
        game = self.games[self.index]
        subprocess.Popen(["python3", game["file"]])

    def draw(self, screen):
        screen.fill((15,15,20))

        title = self.big_font.render("AKOEMU", True, (0,200,255))
        screen.blit(title, (50,50))

        center_x = screen.get_width() // 2
        center_y = screen.get_height() // 2

        for i, game in enumerate(self.games):
            offset = i * 300 - self.scroll_x
            x = center_x + offset
            y = center_y

            dist = abs(offset)
            size = max(120, int(220 - min(dist * 0.3, 80)))

            rect = pygame.Rect(0,0,size,size)
            rect.center = (x,y)

            color = (0,200,255) if i == self.index else (100,100,100)

            pygame.draw.rect(screen, color, rect, border_radius=25)

            text = self.font.render(game["name"], True, (255,255,255))
            screen.blit(text, (x - text.get_width()//2, y + size//2 + 10))