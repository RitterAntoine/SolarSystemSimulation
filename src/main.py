# main.py

import pygame
import sys
import time

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1600
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
GLOBAL_FONT_SIZE = 24
CLOCK_FONT_SIZE = 64


def initialize_simulation():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Simulation du Système Solaire")
    global_font = pygame.font.Font(None, GLOBAL_FONT_SIZE)
    clock_font = pygame.font.Font(None, CLOCK_FONT_SIZE)
    return screen, global_font, clock_font

def render_current_clock(screen, font, color, position):
    current_clock = time.strftime("%H:%M:%S")
    text = font.render(current_clock, True, color)
    screen.blit(text, position)

def run_simulation(screen, global_font, clock_font):

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND_COLOR)
        render_current_clock(screen, clock_font, TEXT_COLOR, (50, 50))
        pygame.display.flip()
        clock.tick(60)

    terminate_simulation()

def terminate_simulation():
    pygame.quit()
    sys.exit()

def main():
    screen, global_font, clock_font = initialize_simulation()
    run_simulation(screen, global_font, clock_font)

if __name__ == "__main__":
    main()