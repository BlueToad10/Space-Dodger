import pygame
#TEXTCOLOUR = (255, 255, 255)

def DrawText(text, fontType, fontSize, textcolour, surface, x, y, Mx, My):
    font = pygame.font.Font(fontType, fontSize)
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = (Mx, My)
    y = y
    pos = x, y
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, textcolour)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height
