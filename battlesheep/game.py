import pygame

from battlesheep.client import make_request
from battlesheep.config import ip_address


def run_pygame(message_queue):
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("IP Address Display")

    # Set up the font
    font = pygame.font.Font(None, 36)

    # Render the IP address text
    text = font.render(f"IP: {ip_address}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(200, 150))

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
