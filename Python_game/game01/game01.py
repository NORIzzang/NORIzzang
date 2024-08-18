import pygame

pygame.init()


background = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NANUL")  # 제목으로 들어가는 부분 생략해도 됨


# 하단의 코드가 없으면 창이 실행됐다가 바로 사라짐
# pygame 을 실행하려면 while 문이 필요함 (반복적으로 실행되게 함)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
            elif event.key == pygame.K_DOWN:
                print("DOWN")
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
            elif event.key == pygame.K_LEFT:
                print("LEFT")

pygame.quit()
