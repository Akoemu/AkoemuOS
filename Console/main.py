import pygame, sys
from launcher import Launcher
from input import InputManager

pygame.init()
pygame.joystick.init()

joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

launcher = Launcher()
input_manager = InputManager()

running = True
while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    input_manager.update(events)
    launcher.update(input_manager)
    launcher.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()