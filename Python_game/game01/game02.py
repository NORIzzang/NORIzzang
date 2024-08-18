import pygame

pygame.init()


background = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NANUL")  # 제목으로 들어가는 부분 생략해도 됨


# 원을 그리고 싶을 때
x_pos = background.get_size()[0]//2  # 400 #위에 background 에있는 800의 반값을 가져오기
y_pos = background.get_size()[1]//2  # 300 #위에 background 에있는 600의 반값을 가져오기

# print(background.get_size())

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
                y_pos = y_pos - 10
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                y_pos = y_pos + 10
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                x_pos = x_pos + 10
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                x_pos = x_pos - 10

    background.fill((255, 0, 0))
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    pygame.draw.circle(surface, color, center, radius)


pygame.quit()
