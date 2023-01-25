import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_dessert():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    dessert = f.generate()
    # Add noise to the fractal shape to make it look more like a dessert
    noise = np.random.normal(0, 0.05, dessert.shape)
    dessert = dessert + noise
    dessert = np.clip(dessert, 0, 1)
    # Apply a dessert-like color map to the fractal shape
    dessert = plt.cm.YlOrBr(dessert)
    # Return the fractal dessert
    return dessert

# Generate 10 fractal dessert images
for i in range(10):
    dessert = generate_fractal_dessert()
    plt.imsave("fractal_dessert_{}.png".format(i), dessert)
