# Perlin-Noise-Generator
### About

**Iam trying to implement perlin noise algorithm in python to use it later in future projects. Perlin noise is a type of procedural noise used in computer graphics and simulations to create natural-looking textures, patterns, and animations. It was developed by Ken Perlin in 1983 and has since become a popular technique for generating realistic landscapes, clouds, fire, and other natural phenomena.**


![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

### **First Milestone: **
            
### Algorihm
i'll be using this [github repo](https://rtouti.github.io/graphics/perlin-noise-algorithm "github repo") and [opengenus repo ](https://iq.opengenus.org/perlin-noise/ "opengenus repo ") as a reference and tutorial for implementing this algorithm, let's walk throught it.

First i called **Numpy** and **Matplot** library, for both math and visualization.

def PerlinNoise(x,y,seed):
    # Creating Permutations table of 512 number so it can wrap up
    permutations = list(range(256))
    shuffle(permutations,seed)
    permutations = np.stack([permutations, permutations]).flatten()
> The algorithm takes as input a certain number of floating point parameters (depending on the dimension) and return a value in a certain range (for Perlin noise, that range is generally said to be between -1.0 and +1.0 but it’s actually a bit different). Let’s say it is in 2 dimensions, so it takes 2 parameters: x and y. Now, x and y can be anything but they are generally a position. To generate a texture, x and y would be the coordinates of the pixels in the texture (multiplied by a small number called the frequency but we will see that at the end). So for texture generation, we would loop through every pixel in the texture, calling the Perlin noise function for each one and decide, based on the return value, what color that pixel would be.
  
    # Getting Grid Coordintaes 
	X =  x.astype(int)
	Y = y.astype(int) 
    # Fraction vectors
    xFract, yFract = x - xCorner, y - yCorner
	
The purpose of the fade function is to modify the influence of the fractional part of the coordinates when calculating the dot product between gradients. It applies a smoothing curve to ensure gradual changes between neighboring values.
```py
def Fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3
 xFaded, yFaded = Fade(xFract), Fade(yFract)
```
Now this can get a little bit tricky, assume this is our grid:


![image](https://github.com/Yousef-Albasel/Perlin-Noise-Generator/assets/111648493/3f3e789b-8814-497b-907a-3c845cb07181)

Each corner has 4 adjacent cells around it, assume we are now dealing with the point (x,y) , we need to find the closest grid point to it, which is (1,1)
there is a restriction : a corner must always get the same value, no matter which of the 4 grid cells that has it as a corner contains the input value.
so for the point (1,1) it's a top right corner for one cell, for the x+1 cell it's a top left corner, and so on .. 
tr = P [ **P[ X+1]** + Y + 1 ] = P [ P [1] + 1] on (0,0)
and tl = P [ **P[ X ]**+Y+1 ] = P [ P [ 1 ]+ 1]   on (1,0)
```py
    bl_val = permutations[permutations[xCorner+1]+yCorner+1]
    tr_val = permutations[permutations[xCorner]+yCorner+1]
    br_val = permutations[permutations[xCorner+1]+yCorner]
    tl_val = permutations[permutations[xCorner]+yCorner]
     
```

    # the code below, created our dot product for each pixel , also creating the constant vector for each pixel , depending on the val we get from t he permutation table which changes for each distinct seed 

    dotTopLeft = dotProduct(tl_val,xFract, yFract)
    dotTopRight = dotProduct(tr_val,xFract, yFract-1)
    dotBottomLeft = dotProduct(bl_val,xFract-1, yFract-1)
    dotBottomRight = dotProduct(br_val,xFract-1, yFract)
Now that we have to dot product for each corner, we need to somehow mix them to get a single value. For this, we’ll use interpolation. Interpolation is a way to find what value lies between 2 other values (say, a1 and a2), given some other value t between 0.0 and 1.0 (a percentage basically, where 0.0 is 0% and 1.0 is 100%). For example: if a1 is 10, a2 is 20 and t is 0.5 (so 50%), the interpolated value would be 15 because it’s midway between 10 and 20 (50% or 0.5). Another example: a1=50, a2=100 and t=0.4. Then the interpolated value would be at 40% of the way between 50 and 100, that is 70. This is called linear interpolation because the interpolated values are in a linear curve.
```py
    first_lerp= lerp(dotTopLeft,dotBottomRight,xFaded)
    second_lerp = lerp(dotTopRight,dotBottomLeft,xFaded)
    return lerp(first_lerp,second_lerp,yFaded)
```
and this creates this beautiful perlin noise 

![image](https://github.com/Yousef-Albasel/Perlin-Noise-Generator/assets/111648493/0e46589f-a1f7-4d7d-a3ed-18f24f4e3a84)
