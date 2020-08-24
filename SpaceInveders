This a game created by me which is based ont the game space invaders which contains similar type of game features from space invaders.

  import pygame
  from pygame import mixer
  import random
  import math

  #initializing pygame
  pygame.init()

  #setting the window for game execution
  screen = pygame.display.set_mode((800, 600))

  #creating icons, labels, and background colour
  pygame.display.set_caption("Space Invaders")
  icon = pygame.image.load("spaceship.png")
  pygame.display.set_icon(icon)

  #Inserting the player
  player_img =  pygame.image.load("player.png")
  playerX = 380
  playerY = 470
  playerX_change= 0

  #Inserting the enemy
  enemy_img = []
  enemyX = []
  enemyY = []
  enemyX_change = []
  enemyY_change = []
  num_of_enemies = 5
  for i in range(num_of_enemies):
      enemy_img.append(pygame.image.load("monster.png"))
      enemyX.append(random.randint(0, 735))
      enemyY.append(random.randint(30, 120))
      enemyX_change.append(1)
      enemyY_change.append(45)

  #Inserting the bullets
  bullet_img = pygame.image.load("bullet.png")
  bulletX = 0
  bulletY = 470
  bulletX_change = 0
  bulletY_change = 2
  bullet_state = "ready"

  #score
  score = 0
  font = pygame.font.Font("font.ttf", 30)
  scoreX = 10
  scoreY = 10

  #game over
  over_font = pygame.font.Font("font.ttf", 70)

  def show_score(x, y):
      show = font.render("SCORE: " + str(score), True, (255,255,255))
      screen.blit(show, (x, y))
  #background
  background = pygame.image.load("Space.png.jpg")

  def player(playerX, playerY):
      screen.blit(player_img, (playerX, playerY))

  def enemy(playerX, playerY, i):
      screen.blit(enemy_img[i], (playerX, playerY))

  def fire_bullet(x, y):
      global bullet_state
      bullet_state = "fire"
      screen.blit(bullet_img,(x + 16, y + 10))

  def collision(enemyX, enemyY, bulletX, bulletY):
      distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
      if distance <= 27: 
          return True
      else:
          return False

  def game_over():
      show_font = over_font.render("GAME OVER", True, (255,255,255))
      screen.blit(show_font, (200,200))

  #Game loop
  main = True
  while main:

      screen.fill((0, 0, 0))
      screen.blit(background,(0,0))

      for event in pygame.event.get():

          #if the player wants to quit the game
          if event.type == pygame.QUIT:
              main = False

          #Key movements in the game
          if event.type ==pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                  playerX_change = -2.34

              if event.key == pygame.K_RIGHT:
                  playerX_change = 2.34

              if event.key == pygame.K_SPACE:
                  if bullet_state == "ready":
                      bullet_sound = mixer.Sound("Laser-shot.wav")
                      bullet_sound.play()

                      bulletX = playerX    
                      fire_bullet(bulletX, bulletY) 

          if event.type == pygame.KEYUP:
                  playerX_change = 0

      #Player movement
      playerX += playerX_change

      if playerX <= 0:
          playerX = 0
      elif playerX >= 736:
          playerX = 736

      #Enemy movement
      for i in range(num_of_enemies):
          if enemyY[i] > 470:
              for j in range(num_of_enemies):
                  enemyY[j] = 2000

              game_over()
              break


          enemyX[i] += enemyX_change[i]
          if enemyX[i] <= 0:
              enemyX_change[i] = 1.67
              enemyY[i] += enemyY_change[i]
          elif enemyX[i] >= 736:
              enemyX_change[i] = -1.67
              enemyY[i] += enemyY_change[i]

               #collision detection 
          collide = collision(enemyX[i], enemyY[i], bulletX, bulletY)
          if collide:
              collide_sound = mixer.Sound("gunshot.wav")
              collide_sound.play()

              bulletY = 470
              bullet_state = "ready"
              score += 2
              print(score)
              enemyX[i] = random.randint(0, 735)
              enemyY[i] = random.randint(30,120)

          enemy(enemyX[i], enemyY[i], i)


      #Bullet movement
      if bulletY == 0:
          bulletY = 470
          bullet_state = "ready"

      if bullet_state == "fire":
          fire_bullet(bulletX, bulletY)
          bulletY -= bulletY_change 



      player(playerX, playerY)
      show_score(scoreX, scoreY)
      pygame.display.update()


