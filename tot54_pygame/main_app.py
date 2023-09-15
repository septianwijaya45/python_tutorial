# install terlebih dahulu => pip install pygame
import pygame

#####=== INIT ===#####
pygame.init()
# run variable
isRun = True

# Display
wL = 500
wP = 500
window = pygame.display.set_mode((wL, wP))

# object game #
# posisi
x=250
y=250

# ukuran
panjang=20
lebar=20

# kecepatan gerak
speed = 5

# run program
while isRun:
    pygame.time.delay(10 )
    #####=== USER INPUT, DB INPUT ===#####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    #####=== Keyboard Press ===#####
    keys = pygame.key.get_pressed()

    # kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # kanan
    if keys[pygame.K_RIGHT] and x < wL-lebar:
        x += speed

    # bawah
    if keys[pygame.K_DOWN] and y < wP-panjang:
        y += speed
    # atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    

    #####=== UPDATE ASSET ===#####
    window.fill((255,255,255)) # background program
    pygame.draw.rect(window, (255,120,0), (x,y,panjang,lebar))
    #####=== RENDER KE DISPLAY ===#####
    pygame.display.update()
pygame.quit()

#####=== INIT ===#####
