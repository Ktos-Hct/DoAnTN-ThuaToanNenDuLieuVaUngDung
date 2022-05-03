#!/usr/bin/python

import os
import pygame
import time
import pyrebase
config = {
    "apiKey": "AIzaSyATfhIehc5XZThp6Z3Mc4xeeZzfgy33Iks",
    "authDomain": "doantn-e31d0-default-rtdb.firebaseio.com",
    "databaseURL": "https://doantn-e31d0-default-rtdb.firebaseio.com",
    "storageBucket": "doantn-e31d0",
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()
def FindImageFilename(lis):
  for filename in os.listdir("."):
    if filename.lower().endswith(".bmp") : lis.append(filename)
    if filename.lower().endswith(".gif") : lis.append(filename)
    if filename.lower().endswith(".jpg") : lis.append(filename)
    if filename.lower().endswith(".png") : lis.append(filename)
  return ""

def FindDisplayDriver():
  for driver in ["fbcon", "directfb", "svgalib"]:
    if not os.getenv("SDL_VIDEODRIVER"):
      os.putenv("SDL_VIDEODRIVER", driver)
    try:
      pygame.display.init()
      return True
    except pygame.error:
      pass
  return False

def Main():
  a=list()
  filename = FindImageFilename(a)
  if filename == "":
    print("No image file found")
  else:
    pygame.init()
    if not FindDisplayDriver():
      print("Failed to initialise display driver")
    else:
      width  = pygame.display.Info().current_w
      height = pygame.display.Info().current_h
      screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
      pygame.mouse.set_visible(False)
      image = pygame.image.load(filename)
      if True:
        image = pygame.transform.scale(image, (width,height))
      screen.blit(image,(0,0))
      running = True
      while running:
        pygame.display.update()
        people=db.child("diekien").get()
        print(people.val())
        if people.val():
              break
    pygame.quit()

if __name__ == "__main__":
  Main()

