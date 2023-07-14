import numpy as np
import matplotlib.pyplot as plot
import random

    
def shuffle(array_to_shuffle, seed):
    random.seed(seed)
    for e in range(len(array_to_shuffle) - 1, 0, -1):
        index = random.randint(0, e - 1)
        temp = array_to_shuffle[e]
        array_to_shuffle[e] = array_to_shuffle[index]
        array_to_shuffle[index] = temp
        
def dotProduct(c, x, y):
    h = c & 3
    vectors = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])
    vec = vectors[h]
    return vec[:,:,0] * x + vec[:,:,1]*y

def Fade(f):
    return 6 * f**5 - 15 * f**4 + 10 * f**3

def lerp(a, b, x):
    "linear interpolation i.e dot product"
    return a + x * (b - a)

def PerlinNoise(x,y,seed):
    # Creating Permutations table of 512 number

    permutations = list(range(256))
    shuffle(permutations,seed)
    permutations = np.stack([permutations, permutations]).flatten()

    # The algorithm takes as input a certain number of floating point parameters (depending on the dimension) and return a value in a certain range (for Perlin noise, that range is generally said to be between -1.0 and +1.0 but it’s actually a bit different). Let’s say it is in 2 dimensions, so it takes 2 parameters: x and y. Now, x and y can be anything but they are generally a position. To generate a texture, x and y would be the coordinates of the pixels in the texture (multiplied by a small number called the frequency but we will see that at the end). So for texture generation, we would loop through every pixel in the texture, calling the Perlin noise function for each one and decide, based on the return value, what color that pixel would be.
  
    # Getting Grid Coordintaes 
    xCorner =  x.astype(int)
    yCorner = y.astype(int) 

    # Fraction vectors
    xFract, yFract = x - xCorner, y - yCorner

    # The purpose of the faded function is to modify the influence of the fractional part of the coordinates when calculating the dot product between gradients. It applies a smoothing curve to ensure gradual changes between neighboring values.

    xFaded, yFaded = Fade(xFract), Fade(yFract)



    # now look at these , there are the  values we will use to create the constant vector, and do the dot product between the distance vector we created above and the constant vector 

    bl_val = permutations[permutations[xCorner+1]+yCorner+1]
    tr_val = permutations[permutations[xCorner]+yCorner+1]
    br_val = permutations[permutations[xCorner+1]+yCorner]
    tl_val = permutations[permutations[xCorner]+yCorner]
     
    # the code below, created our dot product for each pixel , also creating the constant vector for each pixel , depending on the val we get from t he permutation table which changes for each distinct seed 

    dotTopLeft = dotProduct(tl_val,xFract, yFract)
    dotTopRight = dotProduct(tr_val,xFract, yFract-1)
    dotBottomLeft = dotProduct(bl_val,xFract-1, yFract-1)
    dotBottomRight = dotProduct(br_val,xFract-1, yFract)

    # Now that we have to dot product for each corner, we need to somehow mix them to get a single value. For this, we’ll use interpolation. Interpolation is a way to find what value lies between 2 other values (say, a1 and a2), given some other value t between 0.0 and 1.0 (a percentage basically, where 0.0 is 0% and 1.0 is 100%). For example: if a1 is 10, a2 is 20 and t is 0.5 (so 50%), the interpolated value would be 15 because it’s midway between 10 and 20 (50% or 0.5). Another example: a1=50, a2=100 and t=0.4. Then the interpolated value would be at 40% of the way between 50 and 100, that is 70. This is called linear interpolation because the interpolated values are in a linear curve.
        

    # Now do linear interpolation , top left with bottom right, and top right with bottom left , and do both together
    first_lerp= lerp(dotTopLeft,dotBottomRight,xFaded)
    second_lerp = lerp(dotTopRight,dotBottomLeft,xFaded)
    return lerp(first_lerp,second_lerp,yFaded)



arr = np.linspace(1, 10, 500, endpoint=False)

x, y = np.meshgrid(arr, arr)  
plot.imshow(PerlinNoise(x, y,1), origin = 'upper',cmap='gray')

plot.show()