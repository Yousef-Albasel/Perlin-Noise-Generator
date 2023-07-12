# Perlin-Noise-Generator
### About

**Iam trying to implement perlin noise algorithm in python to use it later in future projects. Perlin noise is a type of procedural noise used in computer graphics and simulations to create natural-looking textures, patterns, and animations. It was developed by Ken Perlin in 1983 and has since become a popular technique for generating realistic landscapes, clouds, fire, and other natural phenomena.**


![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

### **First Milestone: **
first milestone is to create a simple perlin noise generator using pygame and numpy, i chose pygame as a graphics engine because i have prior knowledge on how to use it, and numpy for math.

i started by creating a 4* 4 grid : 
```py
def drawGrid():
        blockSize = 128
        cellNumber =(SCREEN_WIDTH/blockSize)
        for x in range(0, SCREEN_WIDTH, blockSize):
            for y in range(0, SCREEN_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, "white", rect, 1)
				```
![image](https://github.com/Yousef-Albasel/Perlin-Noise-Generator/assets/111648493/be89124b-3d1b-4695-8fd9-cb75ccf11885)
