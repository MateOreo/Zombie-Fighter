import pyxel
import time


def movementP1(xPos):
    if pyxel.btn(pyxel.KEY_D):
        xPos += 20

    elif pyxel.btn(pyxel.KEY_A):
        xPos -= 20

    return xPos

def movementP2(xPos):
    if pyxel.btn(pyxel.KEY_RIGHT):
        xPos += 20

    elif pyxel.btn(pyxel.KEY_LEFT):
        xPos -= 20

    return xPos

def jump(yPos):
    jumpVelocity = 0


    if pyxel.btn(pyxel.KEY_W):
        yPos -= jumpVelocity
    return yPos

def gravitation(rect_y, height, gravity, velocity):
    if rect_y + 248 <= height:
        velocity += gravity
        rect_y += velocity

    if rect_y + 248 >= height:  #248 ist die Größe vom Spieler auf der Y-Achse
        velocity = 0

    return rect_y, velocity

def punch_p1(pIsPunching, pLastPunchTime):
    if pyxel.btnp(pyxel.KEY_G) and time.time() - pLastPunchTime >= 0.5:
        print("Differenz: " , time.time() - pLastPunchTime)
        pIsPunching = True
        pLastPunchTime = time.time()
    else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist
        pIsPunching = False
    return pIsPunching, pLastPunchTime

def punch_p2(pIsPunching, pLastPunchTime):
    if pyxel.btnp(pyxel.KEY_KP_5) and time.time() - pLastPunchTime >= 0.5:
        print("Differenz: " , time.time() - pLastPunchTime)
        pIsPunching = True
        pLastPunchTime = time.time()
    else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist
        pIsPunching = False
    return pIsPunching, pLastPunchTime
