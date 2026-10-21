import pygame

pygame.init()
SCREEN_WIDTH , SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Image to the Screen")

background_image = pygame.transform.scale(pygame.image.load("bg.jpg").convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))

ice_image = pygame.transform.scale(pygame.image.load("icey.jpg").convert_alpha(),(200,200))

ice_rect = ice_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))

text = pygame.font.Font(None, 40).render("hello world", True,pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 110))

def gameloop():
    Clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image,(0,0))
        screen.blit(ice_image, ice_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()
        Clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    gameloop()