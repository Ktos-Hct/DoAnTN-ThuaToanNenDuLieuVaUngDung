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

class xulyanh():
    def __init__(self) -> None:
        self.width  = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.width,self.height), pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)
    def capnhathinhanh(self,a):
        image = pygame.image.load(a)
        if True:
            image = pygame.transform.scale(image, (self.width,self.height))
        self.screen.blit(image,(0,0))
        pygame.display.update()
        return 0           
def Main():
    a=list()
    FindImageFilename(a)
    if not a:
            print("No image file found")
    else:
        pygame.init()
        if not FindDisplayDriver():
            print("Failed to initialise display driver")
        else:
            hinhnen=xulyanh()
            running = True
            while running:
                for i in a:
                    hinhnen.capnhathinhanh(i)
                    people=db.child("diekien").get()
                    print(people.val())
                    if people.val():
                        break
                if people.val():
                        break
        pygame.quit()

if __name__ == "__main__":
    Main()

