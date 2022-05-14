import imp
import mcpi.minecraft as minecraft
import mcpi.block as block
import glob
import time
import random

mc = minecraft.Minecraft.create()

SIZEX = 10
SIZEY = 10
SIZEZ = 10
roomx = 1
roomy = 1
roomz = 1

def buildRoom(x, y, z):
    print("buildRoom")

def demolishRoom():
    print("demolishRoom")

def cleanRoom():
    print("cleanRoom")

def listFiles():
    print("listFiles")

def scan3D(filename, originx, originy, originz):
    print("scan3D")

def print3D(filename,originx, originy, originz):
    print("print3D")


def menu():
    print("menu")
    time.sleep(1)
    return random.randint(1,7)

anotherGo = True
while anotherGo:
    choice = menu()
    if choice == 1:
        pos = mc.player.getTilePos()
        buildRoom(pos.x, pos.y, pos.z)
    elif choice == 2:
        listFiles()
    elif choice == 3:
        filename = input("filename?")
        scan3D(filename, roomx+1, roomy+1, roomz+1)
    elif choice == 4:
        filename = input("filename?")
        print3D(filename, roomx+1, roomz+1, roomz+1)
    elif choice == 5:
        scan3D("scantemp", roomx+1, roomy+1, roomz+1)
        pos = mc.player.getTilePos()
        print3D("scantemp", pos.x+1, pos.y, pos.z+1)
    elif choice == 6:
        cleanRoom()
    elif choice == 7:
        demolishRoom()
    elif choice == 8:
        anotherGo = False