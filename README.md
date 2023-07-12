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

now i need to find coords for each corner in the grid, so i added this to the drawGrid method

```py
            # Calculate the corners of each cell
            top_left = (x, y)
            top_right = (x + blockSize, y)
            bottom_left = (x, y + blockSize)
            bottom_right = (x + blockSize, y + blockSize)
            
            corners.append((top_left, top_right, bottom_left, bottom_right))
```

![image](https://github.com/Yousef-Albasel/Perlin-Noise-Generator/assets/111648493/684315ef-7513-4a9f-8836-8b1ae4fa8d27)

now that i have a list of corners, i need to assign a pusedo random vector to it. 
