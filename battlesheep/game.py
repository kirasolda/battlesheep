from queue import Queue

import pygame

from battlesheep.client import make_request
from battlesheep.config import ip_address


class BSGame:

    def __init__(self, inbound_queue: Queue):
        self.inbound_queue = inbound_queue

        pygame.init()
        self.screen = pygame.display.set_mode(
            (800, 600)
        )  # TODO: Think about resolution
        pygame.display.set_caption("BattleSheepGame")
        self.status = "nickname"

    def launch(self) -> None:
        # pages = [self.nickname_page]
        widgets = self.nickname_page()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            # for page in pages:

            for widget in widgets:
                content, rect = widget
                # pygame.draw.rect(self.screen, (0, 0, 255), rect)
                if content:
                    self.screen.blit(content, rect)
                else:
                    pygame.draw.rect(self.screen, (0, 0, 255), rect)

            pygame.display.flip()

    def nickname_page(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Enter nickname", True, (255, 255, 255))
        text_rect = text.get_rect(center=(200, 150))

        text_pair = (text, text_rect)

        input_box = pygame.Rect(100, 100, 200, 40)

        input_pair = (None, input_box)

        # pygame.draw.rect(self.screen, (0, 0, 255), input_box)

        return [text_pair, input_pair]


def run_pygame(message_queue):
    # Initialize pygame

    # Set up the font

    # Render the IP address text

    # Add button "Send message"
    button_font = pygame.font.Font(None, 24)
    button_text = button_font.render("Send message", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(200, 250))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    make_request()

        if not message_queue.empty():
            message = message_queue.get()
            # Update the text with the new message
            text = font.render(f"Message: {message}", True, (255, 255, 255))

        # Fill the screen with a color
        screen.fill((0, 0, 0))

        # Draw the text
        pygame.draw.rect(screen, (0, 0, 255), button_rect.inflate(20, 10))
        screen.blit(button_text, button_rect)
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
